"""The committed scan page matches a fresh build from scan/out/final_ranked.csv."""
import importlib.util, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_scan_page_is_current():
    spec = importlib.util.spec_from_file_location("build_page", os.path.join(ROOT, "scan", "build_page.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)   # builds the html string without writing (writing is under __main__)
    assert open(mod.OUT).read() == mod.html, "scan page is stale: run python3 scan/build_page.py"
