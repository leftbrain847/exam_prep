"""Record Listen mode's summaries at build time with the approved voice (Kokoro af_heart, as in the Field Guide).

    pip install -r build/requirements-audio.txt
    python3 build/audio.py courses/tx_lah --models DIR [topic ...]   # DIR holds course.json audio.model_files

One MP3 per topic with every concept's "name. summary", plus its marks, in the course's audio.dir (repo-relative).
A topic is re-recorded only when its spoken text or audio settings change (the hash). build.py inlines the marks;
the page plays <dir>/<topic>.mp3 from each concept's start to its end, so Listen keeps playing in the background
and on the lock screen, and repeat (x2, x3) replays the recorded clip. Ported from leftbrain847/field_guide.
"""
import hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from build import course  # noqa: E402

HASHED = ["engine", "voice", "lead_in_s", "gap_s", "level_rms_dbfs", "fade_in_s", "fade_out_s", "bitrate_kbps",
          "sample_rate"]


def summary_text(c: dict) -> str:
    """Must match build/listen.js conceptText(c, "summary")."""
    return (c["n"] + ". " + c["s"]).replace("..", ".")


def topic_hash(t: dict, a: dict) -> str:
    spoken = [summary_text(c) for c in t["concepts"]]
    return hashlib.sha256(json.dumps([spoken] + [a[k] for k in HASHED]).encode()).hexdigest()[:16]


def out_dir(a: dict) -> str:
    return os.path.join(ROOT, a["dir"])


def record(t: dict, k, a: dict) -> list[dict]:
    import numpy as np
    rate = 24000
    lead = np.zeros(int(a["lead_in_s"] * rate), np.float32)
    gap = np.zeros(int(a["gap_s"] * rate), np.float32)
    parts, marks, pos = [lead], [], len(lead)
    for ci, c in enumerate(t["concepts"]):
        x, rate = k.create(summary_text(c), voice=a["voice"], speed=1.0, lang=a["lang"])
        x = np.asarray(x, np.float32)
        act = x[np.abs(x) > 0.01]
        if len(act):
            x = np.clip(x * (10 ** (a["level_rms_dbfs"] / 20) / float(np.sqrt(np.mean(act ** 2)))), -1, 1)
        fi, fo = min(len(x), int(a["fade_in_s"] * rate)), min(len(x), int(a["fade_out_s"] * rate))
        if fi:
            x[:fi] *= np.linspace(0, 1, fi, dtype=np.float32)   # Kokoro's onset burst clicks if unfaded
        if fo:
            x[-fo:] *= np.linspace(1, 0, fo, dtype=np.float32)
        marks.append({"ci": ci, "start": round(pos / rate, 3), "end": round((pos + len(x)) / rate, 3)})
        parts += [x, gap]
        pos += len(x) + len(gap)
    pcm = (np.concatenate(parts) * 32767).astype("<i2").tobytes()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", str(rate), "-ac", "1", "-i", "pipe:0",
                    "-ar", str(a["sample_rate"]), "-ac", "1", "-b:a", f"{a['bitrate_kbps']}k",
                    os.path.join(out_dir(a), t["id"] + ".mp3")], input=pcm, check=True)
    return marks


def main(argv: list[str]) -> None:
    cdir = argv[0]
    models = argv[argv.index("--models") + 1] if "--models" in argv else os.environ.get("TTS_MODEL_DIR", "models")
    only = [x for x in argv[1:] if not x.startswith("--") and x != models]
    c = course(cdir)
    a = c["audio"]
    os.makedirs(out_dir(a), exist_ok=True)
    voice = None
    for tid in c["order"]:
        if only and tid not in only:
            continue
        t = json.load(open(os.path.join(cdir, "topics", f"topic-{tid}.json")))
        meta = os.path.join(out_dir(a), tid + ".json")
        h = topic_hash(t, a)
        if not only and os.path.exists(meta) and json.load(open(meta)).get("hash") == h:
            continue
        if voice is None:
            from kokoro_onnx import Kokoro
            voice = Kokoro(*[os.path.join(models, f) for f in a["model_files"]])
        marks = record(t, voice, a)
        json.dump({"hash": h, "file": f"{a['dir']}/{tid}.mp3", "marks": marks}, open(meta, "w"), indent=0)
        print(tid, len(marks), "concepts", round(marks[-1]["end"] / 60, 1), "min", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
