"""Course tests: every topic file passes the writing rules, every outline subsection is covered, the page is current.

    pytest -q
"""
import json, os, re, sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "build"))
sys.path.insert(0, os.path.join(ROOT, "tests"))
import build  # noqa: E402
from check_topic import errors  # noqa: E402

COURSES = sorted(d for d in os.listdir(os.path.join(ROOT, "courses"))
                 if os.path.exists(os.path.join(ROOT, "courses", d, "course.json")))


def topics(cid):
    cdir = os.path.join(ROOT, "courses", cid)
    for tid in build.course(cdir)["order"]:
        p = os.path.join(cdir, "topics", f"topic-{tid}.json")
        if os.path.exists(p):
            yield tid, p


def outline_subsections(cid):
    """Lettered subsections per outline section, e.g. {'G-II': {'A','B','D'}}, read from outline.md headings and lines."""
    out, sec = {}, None
    for line in open(os.path.join(ROOT, "courses", cid, "outline.md")):
        m = re.match(r"## ((?:G|S)-[IVX]+)", line)
        if m:
            sec = m.group(1)
            out[sec] = set()
            for extra in re.findall(r"\+ ((?:G|S)-[IVX]+)", line):
                out.setdefault(extra, set())
            continue
        m = re.match(r"([A-Z]) [A-Z]", line)
        if sec and m:
            out[sec].add(m.group(1))
    return out


@pytest.mark.parametrize("cid", COURSES)
def test_topics_follow_writing_rules(cid):
    bad = {tid: errors(p) for tid, p in topics(cid)}
    bad = {k: v for k, v in bad.items() if v}
    assert not bad, json.dumps(bad, indent=1)


@pytest.mark.parametrize("cid", COURSES)
def test_every_outline_section_is_covered(cid):
    used = set()
    for _, p in topics(cid):
        for c in json.load(open(p))["concepts"]:
            used.update(c.get("o", []))
    sections = {code.split(".")[0] for code in used}
    subs = {".".join(code.split(".")[:2]) for code in used if code.count(".") >= 1}
    missing = []
    for sec, letters in outline_subsections(cid).items():
        if sec not in sections:
            missing.append(sec)
        missing += [f"{sec}.{L}" for L in sorted(letters) if f"{sec}.{L}" not in subs]
    built = {tid for tid, _ in topics(cid)}
    if built != set(build.course(os.path.join(ROOT, "courses", cid))["order"]):
        pytest.skip(f"not all topics written yet; missing so far: {missing}")
    assert not missing, missing


@pytest.mark.parametrize("cid", COURSES)
def test_page_is_current(cid):
    cdir = os.path.join(ROOT, "courses", cid)
    page = os.path.join(ROOT, build.course(cdir)["page"])
    assert os.path.exists(page), "run python3 build/build.py " + cdir
    assert open(page).read() == build.render(cdir), "page is stale: rerun build/build.py"
