"""Pages load nothing from other origins: no web fonts, stylesheets, scripts or images from CDNs.
The homepage's site check refuses any third-party file that isn't self-hosted or pinned, and J's rule is system
fonts or self-hosted files only."""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = sorted(glob.glob(os.path.join(ROOT, "web", "*.html"))) + [
    os.path.join(ROOT, "build", "template.html"),
    os.path.join(ROOT, "scan", "page_template.html"),
]
REMOTE_LOAD = re.compile(
    r"<(?:link|script|img|iframe|source|video|audio)\b[^>]*\b(?:href|src)=[\"']?(?:https?:)?//"
    r"|@import\s+(?:url\()?[\"']?(?:https?:)?//"
    r"|url\(\s*[\"']?(?:https?:)?//"
    r"|fonts\.(?:googleapis|gstatic)\.com",
    re.I,
)


def test_pages_exist():
    assert len(PAGES) >= 3


def test_no_remote_loads():
    bad = []
    for p in PAGES:
        for m in REMOTE_LOAD.finditer(open(p, encoding="utf-8").read()):
            bad.append(f"{os.path.relpath(p, ROOT)}: {m.group(0)[:80]}")
    assert not bad, "remote loads found:\n" + "\n".join(bad)
