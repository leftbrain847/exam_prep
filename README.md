# exam_prep

Exam-prep courses built on the Mastery Field Guide engine (leftbrain847/field_guide), plus the market scan that
chose which exam to build first.

## Courses
- **Texas Life, Accident & Health** (`courses/tx_lah/`): the Texas General Lines exam (Pearson VUE outline
  effective 2026-09-01, 100 general + 30 Texas law questions). Ten topics, one per outline section; every
  outline item maps to a concept. Page: `web/tx_lah.html`.

Each course is a folder: `course.json` (title, tabs, storage prefix, page path), `outline.md` (the official
outline with item codes), `WRITING.md` (the brief topic writers follow) and `topics/topic-<id>.json`.

## Run
```
python3 build/build.py courses/tx_lah     # writes web/tx_lah.html
```

## Listen voice
Summaries are recorded at build time with Kokoro's `af_heart` voice (the Field Guide's approved voice): one MP3 per
topic in `audio/<course>/summary/`, played concept by concept, so repeat (x2, x3) replays the recording and audio
keeps playing on the lock screen. Full notes use the device voice. Settings: `audio` in `course.json`.
```
pip install -r build/requirements-audio.txt
mkdir -p models && for f in kokoro-v1.0.onnx voices-v1.0.bin; do curl -L -o models/$f https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f; done
python3 build/audio.py courses/tx_lah --models models && python3 build/build.py courses/tx_lah
```
Only topics whose spoken text changed are re-recorded. The homepage copies `audio/tx_lah` next to the page
(showcase `assets: audio/tx_lah`).

## Test
```
pip install pytest && pytest -q
python3 tests/check_topic.py courses/tx_lah/topics/topic-<id>.json   # one topic against the writing rules
```

## Exam scan (`scan/`)
Ranks every certification and license in CareerOneStop's data (6,484 certs, 580 state license families) on
market size, stakes, prep spending, exam fee, how beatable the competition is, written-exam fit and liability,
then verifies the top 100 against sources. Weights live in `scan/rubric.yaml`. The published page
`web/exam_scan.html` is a November 2026 snapshot rebuilt from `scan/out/final_ranked.csv` with
`python3 scan/build_page.py` (`tests/test_scan.py` fails if it drifts). The raw CareerOneStop files aren't
committed: download them from careeronestop.org (Developers, Data downloads) into `scan/data/`.

## Deployed
- Exam scan: homepage Tools section (showcase entry `exam_scan`, file `web/exam_scan.html`).
- Course: homepage (showcase entry `tx_lah`, file `web/tx_lah.html`) once it passes review.
