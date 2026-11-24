"""check_topic: validate one course topic file against the writing brief.

usage: python3 tests/check_topic.py courses/tx_lah/topics/topic-<id>.json
Exit code 1 and a list of errors if anything fails. Also importable (errors(path) -> list[str]).
"""
import json, re, sys

RULES = {
    "concepts": (8, 16),
    "cards": (3, 5),
    "max_words": 300,
    "sections_first": ["Model", "Traps", "Example"],
    "sections_allowed": {"Model", "Traps", "Example", "Exam angle"},
    "allowed_tags": {"p", "ul", "ol", "li", "b", "i", "code", "pre", "div", "br"},
    "o_pattern": r"^(G-(I|II|III|IV|V|VI|VII|VIII|IX)|S-(I|II|III|IV))(\.[A-Z](\.\d+)?)?$",
}


def words(html: str) -> int:
    return len(re.sub(r"<[^>]+>", " ", html).split())


def errors(path: str) -> list[str]:
    try:
        t = json.load(open(path))
    except Exception as e:  # noqa: BLE001 - report any parse failure
        return [f"not valid JSON: {e}"]
    errs = []
    for k in ["id", "title", "updated", "refreshDays", "note", "groups", "concepts", "sources"]:
        if k not in t:
            errs.append(f"missing top-level key {k}")
    if errs:
        return errs
    keys = [g["key"] for g in t["groups"]]
    if keys[0] != "map":
        errs.append("first group must be 'map'")
    lo, hi = RULES["concepts"]
    if not lo <= len(t["concepts"]) <= hi:
        errs.append(f"{len(t['concepts'])} concepts; need {lo}-{hi}")
    if t["concepts"] and t["concepts"][0]["g"] != "map":
        errs.append("first concept must be in group 'map'")
    names = set()
    for c in t["concepts"]:
        n = c.get("n", "?")
        if n in names:
            errs.append(f"duplicate concept name: {n}")
        names.add(n)
        if c.get("g") not in keys:
            errs.append(f"{n}: group {c.get('g')} not declared")
        s = c.get("s", "")
        s_plain = re.sub(r"\b(Sec|Secs|No|vs|e\.g|i\.e|U\.S|Inc|Jr|St|Ch|Art|approx)\.", "", s)
        if not s or len(re.findall(r"[.!?]\s+[A-Z]", s_plain.strip())) > 0:
            errs.append(f"{n}: summary must be exactly one sentence")
        titles = [x["t"] for x in c.get("x", [])]
        if titles[:3] != RULES["sections_first"]:
            errs.append(f"{n}: sections must start Model, Traps, Example (got {titles})")
        for x in titles:
            if x not in RULES["sections_allowed"]:
                errs.append(f"{n}: unexpected section '{x}'")
        body = " ".join(x.get("b", "") for x in c.get("x", []))
        w = words(s) + words(body)
        if w > RULES["max_words"]:
            errs.append(f"{n}: {w} words (max {RULES['max_words']})")
        for tag in re.findall(r"</?([a-zA-Z0-9]+)", body):
            if tag.lower() not in RULES["allowed_tags"]:
                errs.append(f"{n}: tag <{tag}> not allowed")
        if re.search(r"\[\d+\]", body):
            errs.append(f"{n}: citation markers like [1] not allowed")
        cards = c.get("cards", [])
        clo, chi = RULES["cards"]
        if not clo <= len(cards) <= chi:
            errs.append(f"{n}: {len(cards)} cards; need {clo}-{chi}")
        for k in cards:
            if not k.get("q") or not k.get("a"):
                errs.append(f"{n}: card missing q or a")
            if "<" in k.get("a", ""):
                errs.append(f"{n}: card answers are plain text")
        o = c.get("o")
        if not o:
            errs.append(f"{n}: missing outline codes 'o'")
        else:
            for code in o:
                if not re.match(RULES["o_pattern"], code):
                    errs.append(f"{n}: bad outline code {code}")
    if not 8 <= len(t["sources"]) <= 25:
        errs.append(f"{len(t['sources'])} sources; need 8-25")
    for s in t["sources"]:
        if not str(s.get("url", "")).startswith("http"):
            errs.append(f"source without a full URL: {s}")
    return errs


if __name__ == "__main__":
    e = errors(sys.argv[1])
    print("\n".join(e) if e else "OK")
    sys.exit(1 if e else 0)
