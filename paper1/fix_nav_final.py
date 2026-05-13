from pathlib import Path
import re

ROOT = Path(r"C:\Myagmardorj")

platform_pages = [
    ROOT / "index.html",
    ROOT / "intro.html",
    ROOT / "landscape.html",
    ROOT / "verify.html",
    ROOT / "roadmap.html",
    ROOT / "contact.html",
]

paper_pages = list((ROOT / "paper1").glob("*.html"))

MASTER_CSS = """
/* === FINAL MASTER NAV FOOTER === */
[data-li]{display:none!important;}
body.en [data-li="en"]{display:inline!important;}
body.mn [data-li="mn"]{display:inline!important;}

body{padding-top:56px!important;padding-bottom:52px!important;}

nav.MN{
  position:fixed!important;
  top:0!important;left:0!important;right:0!important;
  z-index:9999!important;
  height:48px!important;
  display:flex!important;
  align-items:center!important;
  justify-content:space-between!important;
  padding:0 1.5rem!important;
  background:rgba(7,7,16,.98)!important;
  backdrop-filter:blur(22px)!important;
  border-bottom:1px solid rgba(255,255,255,.08)!important;
}

.MN-logo{
  color:#00d4ff!important;
  text-decoration:none!important;
  font-weight:700!important;
  white-space:nowrap!important;
}

.MN-links{display:flex!important;align-items:center!important;gap:.35rem!important;}

.MN-links a,.MN-more button,.MN-foot a{
  color:#9999b8!important;
  text-decoration:none!important;
  padding:.28rem .55rem!important;
  border-radius:7px!important;
  background:none!important;
  border:none!important;
  font-size:.78rem!important;
  cursor:pointer!important;
}

.MN-links a:hover,.MN-links a.MN-cur,.MN-foot a:hover{
  color:#fff!important;
  background:rgba(255,255,255,.07)!important;
}

.MN-more{position:relative!important;}

.MN-dd{
  display:none!important;
  position:absolute!important;
  top:42px!important;
  right:0!important;
  min-width:210px!important;
  padding:.45rem!important;
  background:rgba(12,12,24,.98)!important;
  border:1px solid rgba(255,255,255,.1)!important;
  border-radius:12px!important;
  box-shadow:0 8px 30px rgba(0,0,0,.55)!important;
}

.MN-dd.open{display:block!important;}
.MN-dd a{display:block!important;padding:.38rem .75rem!important;}

.MN-lb{
  font-size:.65rem!important;
  padding:.25rem .55rem!important;
  border:1px solid rgba(255,255,255,.12)!important;
  background:transparent!important;
  color:#777!important;
  cursor:pointer!important;
}
.MN-lb.MN-active{background:#007bff!important;color:#fff!important;}

footer.MN-foot{
  position:fixed!important;
  bottom:0!important;left:0!important;right:0!important;
  z-index:9999!important;
  height:44px!important;
  display:flex!important;
  align-items:center!important;
  justify-content:space-between!important;
  padding:0 1.5rem!important;
  background:rgba(7,7,16,.98)!important;
  backdrop-filter:blur(22px)!important;
  border-top:1px solid rgba(255,255,255,.08)!important;
  font-family:monospace!important;
  font-size:.65rem!important;
  color:#5a5a7a!important;
}

.MN-foot-left{flex:1!important;}
.MN-foot-center{display:flex!important;gap:.25rem!important;align-items:center!important;}
.MN-foot-right{flex:1!important;text-align:right!important;}
"""

MASTER_JS = """
<script>
function MN_toggle(btn){
  var dd = btn.nextElementSibling;
  if(!dd) return;
  dd.classList.toggle('open');
}
document.addEventListener('click', function(e){
  if(!e.target.closest('.MN-more')){
    document.querySelectorAll('.MN-dd').forEach(function(d){ d.classList.remove('open'); });
  }
});
function setLang(l){
  document.body.classList.remove('en','mn');
  document.body.classList.add(l);
  document.querySelectorAll('.MN-lb').forEach(function(b){
    b.classList.toggle('MN-active', b.dataset.l === l);
  });
  try{ localStorage.setItem('lang', l); }catch(e){}
}
document.addEventListener('DOMContentLoaded', function(){
  var l='en';
  try{ l = localStorage.getItem('lang') || 'en'; }catch(e){}
  setLang(l);
});
</script>
"""

PLATFORM_NAV = """
<nav class="MN">
  <a href="/index.html" class="MN-logo">research.nexcore.ltd</a>
  <div class="MN-links">
    <a href="/intro.html"><span data-li="en">Intro</span><span data-li="mn">Танилцуулга</span></a>
    <a href="/landscape.html"><span data-li="en">Landscape</span><span data-li="mn">Хүрээ</span></a>
    <a href="/verify.html"><span data-li="en">Verify</span><span data-li="mn">Шалгах</span></a>
    <a href="/roadmap.html"><span data-li="en">Roadmap</span><span data-li="mn">Зам</span></a>
    <a href="/contact.html"><span data-li="en">Contact</span><span data-li="mn">Холбоо</span></a>
    <a href="/paper1/"><span data-li="en">Research #001</span><span data-li="mn">Судалгаа #001</span></a>
  </div>
  <div>
    <button class="MN-lb" data-l="en" onclick="setLang('en')">ENG</button>
    <button class="MN-lb" data-l="mn" onclick="setLang('mn')">MN</button>
  </div>
</nav>
"""

PLATFORM_FOOTER = """
<footer class="MN-foot">
  <span class="MN-foot-left">Platform · Open archive</span>
  <span class="MN-foot-center">
    <a href="/intro.html">Intro</a>
    <a href="/landscape.html">Landscape</a>
    <a href="/verify.html">Verify</a>
    <a href="/site-map.html">Site Map</a>
  </span>
  <span class="MN-foot-right">v1.0</span>
</footer>
"""

PAPER_NAV = """
<nav class="MN">
  <a href="/" class="MN-logo">Nexcore Research</a>
  <div class="MN-links">
    <a href="/paper1/"><span data-li="en">Results</span><span data-li="mn">Үр дүн</span></a>
    <a href="/paper1/formalism.html"><span data-li="en">Formalism</span><span data-li="mn">Формал тодорхойлолт</span></a>
    <span class="MN-more">
      <button onclick="MN_toggle(this)"><span data-li="en">More ▾</span><span data-li="mn">Дэлгэрэнгүй ▾</span></button>
      <div class="MN-dd">
        <a href="/paper1/charts.html">Charts / Графикууд</a>
        <a href="/paper1/calculator.html">Calculator / Тооцоолол</a>
        <a href="/paper1/lab.html">Analysis Lab / Шинжилгээний лаб</a>
        <a href="/paper1/steven_clark.html">Steven Clark f(x)</a>
        <a href="/paper1/livestats.html">Live Stats / Шууд тоо</a>
        <a href="/paper1/nulltests.html">Null Tests / Null тестүүд</a>
        <a href="/paper1/faq.html">FAQ / Асуулт</a>
        <a href="/paper1/methods.html">Methods / Аргачлал</a>
        <a href="/paper1/references.html">References / Эшлэл</a>
        <a href="/paper1/roadmap.html">Roadmap / Зам</a>
        <a href="/paper1/discussion.html">Discussion / Хэлэлцүүлэг</a>
        <a href="/paper1/about.html">About / Тухай</a>
        <a href="/paper1/replication.html">Replicate / Давтах</a>
        <a href="/paper1/data.html">Data / Өгөгдөл</a>
        <a href="/paper1/changelog.html">Changelog / Өөрчлөлт</a>
      </div>
    </span>
  </div>
  <div>
    <button class="MN-lb" data-l="en" onclick="setLang('en')">ENG</button>
    <button class="MN-lb" data-l="mn" onclick="setLang('mn')">MN</button>
  </div>
</nav>
"""

PAPER_FOOTER = """
<footer class="MN-foot">
  <span class="MN-foot-left">
    <span data-li="en">Computational observations only — not a proof of RH</span>
    <span data-li="mn">Тооцооллын ажиглалт — RH нотолгоо биш</span>
  </span>
  <span class="MN-foot-center">
    <a href="/paper1/">Results</a>
    <a href="/paper1/replication.html">Replicate</a>
    <a href="/paper1/data.html">Data</a>
    <a href="/paper1/about.html">About</a>
  </span>
  <span class="MN-foot-right">
    <a href="https://zenodo.org/records/20077673">DOI</a>
  </span>
</footer>
"""

def strip_all_nav_footer(html):
    # Remove nav and footer tags
    html = re.sub(r"<nav[\s\S]*?</nav>", "", html, flags=re.I)
    html = re.sub(r"<footer[\s\S]*?</footer>", "", html, flags=re.I)
    # Remove old SPA nav inline links
    html = re.sub(r'<a[^>]*class="MN-logo"[^>]*>.*?</a>', "", html)
    # Remove duplicate MASTER_CSS blocks
    parts = html.split("/* === FINAL MASTER NAV FOOTER === */")
    if len(parts) > 2:
        html = parts[0] + "/* === FINAL MASTER NAV FOOTER === */" + parts[-1]
    return html

def inject_css(html, skip_panel_override=False):
    # Remove old MASTER_CSS block first
    html = re.sub(r"/\* === FINAL MASTER NAV FOOTER === \*/[\s\S]*?(?=</style>|$)", "", html)
    # Add fresh CSS
    if "</style>" in html:
        html = html.replace("</style>", MASTER_CSS + "\n</style>", 1)
    else:
        html = html.replace("</head>", f"<style>{MASTER_CSS}</style></head>", 1)
    return html

def inject_js(html):
    # Remove old duplicate master-like scripts only if needed? Safer: add if absent.
    if "function MN_toggle(btn)" not in html:
        html = html.replace("</body>", MASTER_JS + "\n</body>", 1)
    return html

def fix(path, nav, footer):
    html = path.read_text(encoding="utf-8", errors="ignore")
    html = html.replace("data-lang=", "data-li=")
    html = re.sub(r"<body[^>]*>", '<body class="en">', html, count=1, flags=re.I)
    html = strip_all_nav_footer(html)
    html = html.replace('<body class="en">', '<body class="en">\n' + nav, 1)
    html = html.replace("</body>", footer + "\n</body>", 1)
    html = inject_css(html)
    html = inject_js(html)
    path.write_text(html, encoding="utf-8")

for p in platform_pages:
    if p.exists():
        fix(p, PLATFORM_NAV, PLATFORM_FOOTER)

PLATFORM_FILES = {"index.html","intro.html","landscape.html",
                  "verify.html","roadmap.html","contact.html","site-map.html"}

for p in paper_pages:
    if p.name in PLATFORM_FILES:
        continue  # platform файл paper1/-д байвал хөндөхгүй
    if p.name == "steven_clark.html":
        # Only update nav/footer, preserve panel CSS
        html = p.read_text(encoding="utf-8", errors="ignore")
        html = html.replace("data-lang=", "data-li=")
        html = re.sub(r"<body[^>]*>", '<body class="en">', html, count=1, flags=re.I)
        html = strip_all_nav_footer(html)
        html = html.replace('<body class="en">', '<body class="en">\n' + PAPER_NAV, 1)
        html = html.replace("</body>", PAPER_FOOTER + "\n</body>", 1)
        # Only add nav JS, NOT full MASTER_CSS (preserve panel CSS)
        if "function MN_toggle(btn)" not in html:
            html = html.replace("</body>", MASTER_JS + "\n</body>", 1)
        p.write_text(html, encoding="utf-8")
    else:
        fix(p, PAPER_NAV, PAPER_FOOTER)

# Ensure site-map exists
sitemap = ROOT / "site-map.html"
if not sitemap.exists():
    sitemap.write_text("""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Site Map · research.nexcore.ltd</title></head>
<body class="en">
<h1>Site Map</h1>
<ul>
<li><a href="/index.html">Platform Home</a></li>
<li><a href="/intro.html">Intro</a></li>
<li><a href="/landscape.html">Landscape</a></li>
<li><a href="/verify.html">Verify</a></li>
<li><a href="/paper1/">Research #001</a></li>
<li><a href="/paper1/charts.html">Charts</a></li>
<li><a href="/paper1/calculator.html">Calculator</a></li>
<li><a href="/paper1/steven_clark.html">Steven Clark f(x)</a></li>
</ul>
</body></html>
""", encoding="utf-8")

print("FINAL NAV FIX DONE")