"""Generate ED_Streamlined_Theory.xlsx from Foundation.md and the result pages.

The workbook is not maintained by hand. It is built from the markdown in this
repository, so the two cannot drift apart. Edit the markdown, then re-run:

    python tools/build_workbook.py

Requires openpyxl. Overwrites ED_Streamlined_Theory.xlsx in the repository root.
The Counts tab holds live formulas with no stored values; Excel fills them on open.
"""
import io, os, re, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
clean = lambda s: re.sub(r"\*\*|\[|\]\([^)]*\)", "", s).strip()

S = io.open("Foundation.md", encoding="utf-8").read().replace("\r\n", "\n")


def rows(after, stop=None):
    seg = S.split(after, 1)[1]
    if stop:
        seg = seg.split(stop, 1)[0]
    out = []
    for l in seg.split("\n"):
        l = l.strip()
        if l.startswith("|") and "---" not in l:
            c = [x.strip() for x in l.strip("|").split("|")]
            if c and c[0] and c[0].lower() not in ("", "primitive", "constant", "axiom", "condition", "argument", "definition"):
                out.append(c)
    return out


prim = rows("### The 13 primitives", "### The 10 constants")
cons = rows("### The 10 constants", "### The 26 axioms")
ax14 = rows("**14 from the 38 core-theory lines**", "The 38 lines carry one more line")
ax7 = rows("**7 more, found in the foundation papers**", "**5 working conditions")
cond = rows("**5 working conditions for the gravity picture**", "## Arguments")
args = rows("## Arguments (4)", "## Definitions")
defs = rows("## Definitions (3, not counted)")


def split_label(cell):
    m = re.match(r"\*\*(.+?):?\*\*[:\s]*(.*)", cell.strip())
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "", clean(cell)


FOUND = []
for r in prim:
    FOUND.append((r[0], "Primitive", r[0], "", clean(r[1]), "Paper_087", ""))
for r in cons:
    FOUND.append((r[0], "Constant", r[0], "", clean(r[1]), "core 38 lines", ""))
for r in ax14:
    lab, st = split_label(r[1])
    FOUND.append(("A" + r[0], "Axiom", r[0], lab, st, clean(r[2]) if len(r) > 2 else "", ""))
for r in ax7:
    lab, st = split_label(r[1])
    FOUND.append(("A" + r[0], "Axiom", r[0], lab, st, clean(r[2]) if len(r) > 2 else "", clean(r[3]) if len(r) > 3 else ""))
for r in cond:
    lab, st = split_label(r[1])
    FOUND.append(("C" + r[0], "Condition", r[0], lab, st, clean(r[2]) if len(r) > 2 else "", clean(r[3]) if len(r) > 3 else ""))
for r in args:
    lab, st = split_label(r[1])
    FOUND.append(("G" + r[0], "Argument", r[0], lab, st, clean(r[2]) if len(r) > 2 else "", clean(r[3]) if len(r) > 3 else ""))
for r in defs:
    lab, st = split_label(r[1])
    FOUND.append(("D" + r[0], "Definition", r[0], lab, st, clean(r[2]) if len(r) > 2 else "", "not counted"))
FKEY = {f[0]: f for f in FOUND}


def sections(txt):
    out, cur, buf = {}, "_head", []
    for l in txt.split("\n"):
        if l.startswith("## "):
            out[cur] = "\n".join(buf)
            cur, buf = l[3:].strip(), []
        else:
            buf.append(l)
    out[cur] = "\n".join(buf)
    return out


def table(seg):
    out = []
    for l in seg.split("\n"):
        l = l.strip()
        if l.startswith("|") and "---" not in l:
            c = [x.strip() for x in l.strip("|").split("|")]
            if c and c[0].lower() not in ("", "item", "result", "borrowed", "condition"):
                out.append(c)
    return out


def bullets(seg):
    return [clean(l.strip()[2:]) for l in seg.split("\n") if l.strip().startswith("- ")]


def para(seg):
    p = [l.strip() for l in seg.split("\n") if l.strip() and not l.strip().startswith("|")]
    return " ".join(p)


RES = []
for p in sorted(glob.glob("Results/*.md")):
    if p.endswith("README.md"):
        continue
    t = io.open(p, encoding="utf-8").read().replace("\r\n", "\n")
    sec = sections(t)
    head = sec["_head"]
    title = re.search(r"^# (.+)$", head, re.M).group(1).strip()
    claim = clean(re.search(r"\*\*The claim\.\*\*(.+)", head).group(1))
    strength = clean(re.search(r"\*\*Strength:\*\*(.+)", head).group(1))
    m = re.search(r"\*\*Sector:\*\*\s*(.+?)\.\s*\*\*Paper:\*\*\s*\[([^\]]+)\]\([^)]*\)\.\s*\*\*Ledger row:\*\*\s*(\d+)", head)
    RES.append(dict(page=os.path.basename(p), title=title, claim=claim, strength=strength,
                    sector=m.group(1), paper=m.group(2), row=int(m.group(3)),
                    review=bullets(sec.get("What review found", "")),
                    uses=table(sec.get("What it uses from the foundation", "")),
                    prior=table(sec.get("What it uses from earlier ED results", "")),
                    borrow=table(sec.get("What it borrows from standard physics", "")),
                    leans=bullets(sec.get("What this leans on, stated plainly", "")),
                    kill=para(sec.get("How it could be killed", "")),
                    isnot=para(sec.get("What it is not", ""))))


def expand(tok):
    tok = clean(tok)
    out = []
    if tok in ("—", "-", ""):
        return out
    out += re.findall(r"\bP\d{2}\b", tok)
    out += ["A" + m for m in re.findall(r"axiom (\d+)", tok, re.I)]
    rng = re.findall(r"conditions (\d+) to (\d+)", tok, re.I)
    for a, b in rng:
        out += ["C%d" % i for i in range(int(a), int(b) + 1)]
    if not rng:
        out += ["C" + m for m in re.findall(r"condition (\d+)", tok, re.I)]
    out += ["D" + m for m in re.findall(r"definition (\d+)", tok, re.I)]
    out += ["G" + m for m in re.findall(r"argument (\d+)", tok, re.I)]
    for s in re.split(r",| and ", tok):
        s = s.strip()
        if s in FKEY and FKEY[s][1] == "Constant":
            out.append(s)
    return list(dict.fromkeys(out))


wb = Workbook()
ARIAL = "Arial"
H = Font(name=ARIAL, bold=True, color="FFFFFF", size=10)
HF = PatternFill("solid", fgColor="404040")
B = Font(name=ARIAL, size=10)
BB = Font(name=ARIAL, size=10, bold=True)
TITLE = Font(name=ARIAL, bold=True, size=14)
WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")
THIN = Border(bottom=Side("thin", color="D0D0D0"))


def sheet(name, headers, widths, data, wrapcols=()):
    ws = wb.create_sheet(name)
    for i, h in enumerate(headers, 1):
        c = ws.cell(1, i, h)
        c.font = H
        c.fill = HF
        c.alignment = Alignment(vertical="center", wrap_text=True)
    for j, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(j)].width = w
    for r, rowv in enumerate(data, 2):
        for i, v in enumerate(rowv, 1):
            c = ws.cell(r, i, v)
            c.font = B
            c.border = THIN
            c.alignment = WRAP if i in wrapcols else TOP
    ws.freeze_panes = "A2"
    if data:
        ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(len(headers)), len(data) + 1)
    ws.row_dimensions[1].height = 28
    return ws


fdata = [(f[1], f[2], f[3], f[4], f[5], f[6], f[0]) for f in FOUND]
sheet("Foundation", ["Kind", "No.", "Name", "What it says", "Where", "Note", "Key"],
      [12, 6, 30, 78, 16, 46, 8], fdata, wrapcols=(3, 4, 6))

rdata = []
for r in sorted(RES, key=lambda x: x["row"]):
    chain = "yes" if any("band-accounting" in " ".join(d) for d in r["prior"]) else ""
    rdata.append((r["title"], r["sector"], r["claim"], r["strength"], r["row"], r["paper"],
                  ", ".join(clean(u[0]) for u in r["uses"]) or "none directly",
                  "; ".join(clean(b[0]) for b in r["borrow"]) or "none",
                  " | ".join(r["leans"]), r["kill"], r["isnot"], r["page"], chain,
                  " | ".join(r["review"])))
sheet("Results", ["Result", "Sector", "What the paper claims", "Verdict (review 2026-09-12)", "Ledger row", "Source paper",
                  "Foundation items used", "Borrowed from standard physics",
                  "What it leans on", "How it could be killed", "What it is not", "Paper",
                  "On the gravity chain", "What review found"],
      [34, 16, 60, 50, 9, 34, 26, 40, 70, 60, 50, 30, 12, 90], rdata, wrapcols=(1, 3, 4, 6, 7, 8, 9, 10, 11, 14))

udata = []
for r in sorted(RES, key=lambda x: x["row"]):
    seen = []
    for u in r["uses"]:
        for k in expand(u[0]):
            if k in seen:
                continue
            seen.append(k)
            f = FKEY.get(k)
            udata.append((r["title"], r["row"], k, f[1] if f else "?",
                          (f[3] or f[4][:60]) if f else "", clean(u[2]) if len(u) > 2 else ""))
    if not seen:
        udata.append((r["title"], r["row"], "—", "none directly", "runs on earlier ED results", ""))
sheet("Uses Map", ["Result", "Ledger row", "Item key", "Kind", "Item", "How it enters"],
      [34, 9, 10, 12, 44, 60], udata, wrapcols=(1, 5, 6))

ddata = []
for r in sorted(RES, key=lambda x: x["row"]):
    for d in r["prior"]:
        ddata.append((r["title"], clean(d[0]), clean(d[1]) if len(d) > 1 else "",
                      clean(d[2]) if len(d) > 2 else ""))
sheet("Dependencies", ["Result", "Depends on", "What it supplies", "Where that stands"],
      [34, 34, 52, 62], ddata, wrapcols=(1, 2, 3, 4))

pap = []
for f in sorted(glob.glob("Papers/*.md")):
    n = os.path.basename(f)[:-3]
    if n == "README":
        continue
    carries = [r["title"] for r in RES if r["paper"] == n]
    pap.append((n, "result paper", "; ".join(carries) or "(unmatched)", len(carries)))
for f in sorted(glob.glob("Papers/upstream/*.md")):
    n = os.path.basename(f)[:-3]
    if n == "README":
        continue
    pap.append((n, "upstream", "carries no result on this list; holds up the ones that do", 0))
sheet("Papers", ["Paper", "Role", "Results it carries", "Count"], [58, 14, 70, 8], pap, wrapcols=(1, 3))

ws = wb.create_sheet("Counts")
ws["A1"] = "Counts"
ws["A1"].font = TITLE
UM = "'Uses Map'"
lines = [("Foundation", ""),
         ("Primitives", '=COUNTIF(Foundation!$A:$A,"Primitive")'),
         ("Constants", '=COUNTIF(Foundation!$A:$A,"Constant")'),
         ("Axioms", '=COUNTIF(Foundation!$A:$A,"Axiom")'),
         ("Working conditions", '=COUNTIF(Foundation!$A:$A,"Condition")'),
         ("Arguments", '=COUNTIF(Foundation!$A:$A,"Argument")'),
         ("Counted total", "=B4+B5+B6+B7+B8"),
         ("Definitions (not counted)", '=COUNTIF(Foundation!$A:$A,"Definition")'),
         ("", ""),
         ("Results", ""),
         ("Results listed", "=COUNTA(Results!$A$2:$A$100)"),
         ("On the gravity chain", '=COUNTIF(Results!$M:$M,"yes")'),
         ("Using V5 (axiom 14)", '=COUNTIF(' + UM + '!$C:$C,"A14")'),
         ("Using V1 (axiom 21)", '=COUNTIF(' + UM + '!$C:$C,"A21")'),
         ("Using a working condition", '=COUNTIF(' + UM + '!$D:$D,"Condition")'),
         ("Sectors of physics", '=SUMPRODUCT((Results!$B$2:$B$17<>"")/COUNTIF(Results!$B$2:$B$17,Results!$B$2:$B$17&""))'),
         ("", ""),
         ("Review verdicts (2026-09-12)", ""),
         ("Textbook result, restated", '=COUNTIF(Results!$D:$D,"Textbook result*")'),
         ("Modest ED-specific result", '=COUNTIF(Results!$D:$D,"Modest*")'),
         ("Identification, not a derivation", '=COUNTIF(Results!$D:$D,"Identification*")'),
         ("Not established", '=COUNTIF(Results!$D:$D,"Not established*")')]
r = 3
for lab, f in lines:
    c = ws.cell(r, 1, lab)
    c.font = BB if (f == "" and lab) else B
    if f:
        ws.cell(r, 2, f).font = B
    r += 1
ws.column_dimensions["A"].width = 30
ws.column_dimensions["B"].width = 12
ws.column_dimensions["D"].width = 70
ws["D3"] = "Live counts, recalculated from the Foundation, Results, Uses Map and Dependencies tabs. Edit those and these follow."
ws["D3"].font = Font(name=ARIAL, size=10, italic=True)
ws["D3"].alignment = WRAP

NOT = [("Grounded", 132, "Holds given a further local assumption that is not on the foundation page. Outside this list."),
       ("Postulated", 59, "A declared assumption belonging to one paper."),
       ("Open", 51, "Named as unresolved."),
       ("Selected/Inherited", 40, "Taken from published physics."),
       ("Synthesis", 31, "Ties existing results together."),
       ("Prediction", 24, "A falsifiable bet, not yet tested."),
       ("Asserted", 22, "Stated without a supporting argument in the paper."),
       ("Measured", 14, "Measured in the simulator, including row 92 (zero signalling), retiered from Derived on 2026-09-11."),
       ("Primitive", 13, "The primitives themselves; they are on the Foundation tab."),
       ("Derived", 9, "Nine in the ledger, eight of them on this list. Row 42 (the c-power in G) is excluded as unit arithmetic. Review of 2026-09-12: none of the eight holds as a derivation of new content; see the Results tab."),
       ("Constant", 9, "The constants; they are on the Foundation tab."),
       ("D-via-I / Form-forced", 8, "All eight are on this list. Review of 2026-09-12: these are mostly known results restated; see the Results tab.")]
sheet("Not On This List", ["Ledger tier", "Count", "Why it is not on this list"], [26, 8, 100], NOT, wrapcols=(3,))

ws = wb.create_sheet("Read Me", 0)
ws.column_dimensions["A"].width = 118
txt = [("Event Density — an honest account", "t"),
       ("", ""),
       ("What this workbook is", "h"),
       ("The core of Event Density in one file: the 53 items ED starts from, and the 16 results whose papers use nothing beyond them, each with a review verdict.", "b"),
       ("Generated from Foundation.md and the sixteen result pages in this folder. Those documents are the source.", "b"),
       ("", ""),
       ("The one thing to know up front", "h"),
       ("On review (2026-09-12), none of the sixteen derives anything not already known. Six are textbook results restated in ED terms, one is a modest ED-specific result, four are identifications without calculation, and five (all in the gravity block) rest on steps that do not hold as written. ED is an interpretive framework, not yet a theory that can be calculated from.", "b"),
       ("", ""),
       ("The tabs", "h"),
       ("Foundation — all 53 counted items plus the 3 uncounted definitions.", "b"),
       ("Results — the 16, one row each: what the paper claims, the review verdict, what review found, what it uses, borrows and leans on, how to kill it.", "b"),
       ("Uses Map — one row per result-and-item pair. Filter by item key to see everything that uses a given assumption.", "b"),
       ("Dependencies — which results stand on earlier ED results, and where those stand.", "b"),
       ("Papers — the 14 result papers and the 4 upstream papers. Each paper file opens with a review note that takes precedence over its text.", "b"),
       ("Counts — live counts, including the review verdicts.", "b"),
       ("Not On This List — what was left out, and why.", "b"),
       ("", ""),
       ("What the verdicts mean", "h"),
       ("Textbook result, restated: correct, but known physics or mathematics, with ED supplying vocabulary. Modest ED-specific result: a correct statement about an ED model with limited physical reach. Identification: a known phenomenon said to be a substrate object, with nothing calculated. Not established: relies on a step that does not hold as written.", "b"),
       ("", ""),
       ("The rule", "h"),
       ("A result appears here only if its paper uses nothing beyond the Foundation tab. Passing the rule means no hidden assumptions; it does not make a result a derivation.", "b"),
       ("", ""),
       ("Source of record", "h"),
       ("The canonical corpus is the ED Generative repository and its claims ledger, ED_ItemizedTheory_TieredClaims_v2.xlsx. Ledger row numbers on the Results tab point into that ledger. The ledger's tiers predate this review.", "b")]
r = 1
for s, k in txt:
    c = ws.cell(r, 1, s)
    c.font = TITLE if k == "t" else (BB if k == "h" else B)
    c.alignment = WRAP
    if k == "b":
        ws.row_dimensions[r].height = 30
    r += 1

NT = wb["Not On This List"]
nr = NT.max_row + 2
nc = NT.cell(nr, 1, "Source: ED_ItemizedTheory_TieredClaims_v2.xlsx (ED Generative), tier counts as of 2026-09-11. These twelve figures are typed from that ledger, not computed here.")
nc.font = Font(name=ARIAL, size=10, italic=True)
nc.alignment = WRAP
cw = wb["Counts"]
cw["D5"] = "Column B holds formulas with no stored result. Excel fills them in the moment the file opens."
cw["D5"].font = Font(name=ARIAL, size=10, italic=True)
cw["D5"].alignment = WRAP

del wb["Sheet"]
out = "ED_Streamlined_Theory.xlsx"
wb.save(out)
print("saved", out)
print("foundation rows:", len(fdata), "| results:", len(rdata), "| uses map:", len(udata),
      "| deps:", len(ddata), "| papers:", len(pap))
