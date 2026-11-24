"""Build one course page: build/template.html + courses/<id>/topics/topic-*.json -> one self-contained HTML file.

    python3 build/build.py courses/tx_lah        # writes the page named in courses/tx_lah/course.json

Adapted from the Mastery Field Guide's build (leftbrain847/field_guide). Course settings (title, intro, tab
categories, storage prefix, output page) live in the course's course.json, not here. Recorded audio and the
Spanish Listen text are not wired in yet: Listen uses the device voice.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
# Same document wrapper the Field Guide uses, so the page renders in standards mode anywhere.
SKELETON_HEAD = '<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>'
SKELETON_TAIL = "</body></html>"


def course(cdir: str) -> dict:
    c = json.load(open(os.path.join(cdir, "course.json")))
    c["order"] = [t for cat in c["categories"] for t in cat["topics"]]
    return c


def check(t: dict) -> tuple[int, int]:
    keys = {g["key"] for g in t["groups"]}
    for c in t["concepts"]:
        assert c["g"] in keys, (t["id"], c["n"], c["g"])
        assert c["s"] and c["x"], (t["id"], c["n"])
        for k in c.get("cards", []):
            assert k["q"] and k["a"], (t["id"], c["n"])
    return len(t["concepts"]), sum(len(c.get("cards", [])) for c in t["concepts"])


def inline(name: str) -> str:
    src = open(os.path.join(HERE, name)).read()
    assert "</" not in src, f"{name} must not contain '</' (it is inlined in a script tag)"
    return "<script>\n" + src.rstrip("\n") + "\n</script>"


def render(cdir: str, quiet: bool = True) -> str:
    c = course(cdir)
    blocks = []
    for tid in c["order"]:
        p = os.path.join(cdir, "topics", f"topic-{tid}.json")
        if not os.path.exists(p):
            if not quiet:
                print("missing", tid)
            continue
        t = json.load(open(p))
        n = check(t)
        if not quiet:
            print(tid, *n)
        blocks.append(f'<script type="application/json" id="topic-{tid}">'
                      + json.dumps(t, ensure_ascii=False).replace("</", "<\\/") + "</script>")
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html = open(os.path.join(HERE, "template.html")).read()
    html = (html.replace("__TITLE__", esc(c["title"])).replace("__INTRO__", esc(c["intro"]))
            .replace("__CATEGORIES__", json.dumps(c["categories"], ensure_ascii=False))
            .replace("__PLACEHOLDERS__", json.dumps(c["placeholders"], ensure_ascii=False))
            .replace("__PREFIX__", c["prefix"]))
    html = html.replace("<!--TOPICS-->", "\n".join(blocks))
    html = html.replace("<!--LISTEN-->", inline("listen.js")).replace("<!--RECENT-->", inline("recent.js"))
    html = html.replace("<!--ES-->", '<script type="application/json" id="es-text">{}</script>')
    html = html.replace("<!--AUDIO-->", '<script type="application/json" id="audio-marks">{}</script>')
    return SKELETON_HEAD + "\n" + html.rstrip("\n") + "\n\n" + SKELETON_TAIL


if __name__ == "__main__":
    cdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "courses", "tx_lah")
    out = os.path.join(ROOT, course(cdir)["page"])
    html = render(cdir, quiet=False)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(html)
    print("wrote", out, len(html) // 1024, "KB")
