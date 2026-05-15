from pathlib import Path
import re

ROOT = Path(r"C:\Myagmardorj")
ALL_HTML = list(ROOT.glob("*.html")) + list((ROOT / "paper1").glob("*.html"))
REPORT = []

def log(msg):
    print(msg)
    REPORT.append(msg)

def safe_read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def safe_write(p, txt):
    p.write_text(txt, encoding="utf-8")

log("=== PHASE 1–8 QA AUDIT START ===")

for p in ALL_HTML:
    txt = safe_read(p)

    txt = txt.replace("More ▾", "")
    txt = txt.replace("Дэлгэрэнгүй ▾", "")
    txt = txt.replace('href="/paper1/" class="MN-logo">Nexcore Research',
                      'href="/" class="MN-logo">Nexcore Research')

    txt = txt.replace("data-lang=", "data-li=")

    txt = re.sub(r'href="charts.html"',
                 'href="/paper1/charts.html"', txt)

    txt = re.sub(r'href="calculator.html"',
                 'href="/paper1/calculator.html"', txt)

    txt = re.sub(r'href="../paper1/',
                 'href="/paper1/', txt)

    txt = txt.replace('href="#"', 'href="/"')

    if "padding-bottom:52px" in txt:
        txt = txt.replace("padding-bottom:52px",
                          "padding-bottom:72px")

    safe_write(p, txt)

TEMP = [
    "fix_menus.py",
    "fix_nav_final.py",
    "fix_steven_nav.py",
]

for t in TEMP:
    f = ROOT / t
    if f.exists():
        f.unlink()
        log(f"[REMOVED] {t}")

docs = ROOT / "docs"
docs.mkdir(exist_ok=True)

report = docs / "QA_REPORT.txt"
report.write_text("\\n".join(REPORT), encoding="utf-8")

print("===================================")
print("PHASE 1–8 QA AUDIT COMPLETE")
print("===================================")
