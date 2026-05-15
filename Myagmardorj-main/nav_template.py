"""
nav_template.py — НЭГ ЭХ СУРВАЛЖ
===================================
Энэ файлд nav, footer, CSS бүгдийг засна.
Дараа нь: python rebuild_nav.py

Platform nav: 6 link
Paper1 nav:  17 link + ← Platform
"""

# ═══════════════════════════════════
# CSS — нэг удаа засна
# ═══════════════════════════════════
NAV_CSS = """[data-li]{display:none}body.en [data-li=en]{display:inline}body.mn [data-li=mn]{display:inline}
.MN{position:fixed;top:0;left:0;right:0;z-index:900;background:rgba(7,7,16,.96);backdrop-filter:blur(24px);border-bottom:1px solid rgba(255,255,255,.07);padding:.4rem 1.25rem;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.MN-logo{font-family:'Space Grotesk',sans-serif;font-size:.88rem;font-weight:600;background:linear-gradient(135deg,#00d4ff,#4d9fff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-decoration:none;white-space:nowrap;flex-shrink:0}
.MN-sep{width:1px;height:18px;background:rgba(255,255,255,.1);flex-shrink:0}
.MN-links{display:flex;align-items:center;justify-content:center;gap:2px;flex:1;flex-wrap:wrap}
.MN-links a{font-size:.72rem;color:#9999b8;text-decoration:none;padding:3px 6px;border-radius:5px;transition:color .15s,background .15s;white-space:nowrap}
.MN-links a:hover{color:#eeeef8;background:rgba(255,255,255,.07)}
.MN-links a.MN-active{color:#00d4ff;border-bottom:2px solid #00d4ff;padding-bottom:1px}
.MN-plat{font-size:.7rem;color:#5a5a7a;text-decoration:none;padding:3px 8px;border-radius:5px;border:1px solid rgba(255,255,255,.08);white-space:nowrap;flex-shrink:0;transition:color .15s,border-color .15s}
.MN-plat:hover{color:#9999b8;border-color:rgba(255,255,255,.15)}
.MN-btns{display:flex;gap:3px;flex-shrink:0}
.MN-lb{font-family:'JetBrains Mono',monospace;font-size:.62rem;padding:3px 8px;border-radius:4px;cursor:pointer;transition:all .15s;border:1px solid rgba(255,255,255,.1);background:none;color:#5a5a7a}
.MN-lb.on{background:linear-gradient(135deg,#0055ff,#00d4ff);color:#fff;border-color:transparent}
.MN-burger{display:none;flex-direction:column;gap:4px;cursor:pointer;padding:.4rem;border:none;background:none;flex-shrink:0}
.MN-burger span{display:block;width:18px;height:1.5px;background:#9999b8;border-radius:2px;transition:all .25s}
.MN-burger.open span:nth-child(1){transform:rotate(45deg) translate(4px,4px)}
.MN-burger.open span:nth-child(2){opacity:0}
.MN-burger.open span:nth-child(3){transform:rotate(-45deg) translate(4px,-4px)}
.MN-mob{display:none;position:fixed;top:0;left:0;right:0;background:rgba(7,7,16,.98);border-bottom:1px solid rgba(255,255,255,.08);padding:3.5rem 1.25rem 1rem;z-index:899;flex-direction:column;gap:2px}
.MN-mob.open{display:flex}
.MN-mob a{font-size:.82rem;color:#9999b8;text-decoration:none;padding:6px 8px;border-radius:6px}
.MN-mob a:hover,.MN-mob a.MN-active{color:#00d4ff;background:rgba(0,212,255,.07)}
.MN-mob hr{border:none;border-top:1px solid rgba(255,255,255,.07);margin:4px 0}
.MN-foot{position:fixed;bottom:0;left:0;right:0;z-index:500;height:40px;display:flex;align-items:center;padding:0 1.25rem;background:rgba(7,7,16,.98);border-top:1px solid rgba(255,255,255,.07);font-size:.65rem;color:#5a5a7a}
.MN-foot a{color:#5a5a7a;text-decoration:none;padding:2px 5px;border-radius:4px;transition:color .15s}
.MN-foot a:hover{color:#9999b8}
.MN-foot-sep{opacity:.3;margin:0 2px}
@media(max-width:768px){.MN-links,.MN-sep,.MN-plat{display:none}.MN-burger{display:flex}}"""

# ═══════════════════════════════════
# JS — нэг удаа засна
# ═══════════════════════════════════
NAV_JS = """<script>
(function(){
  function setLang(l){
    l=l==='mn'?'mn':'en';
    document.body.className=l;
    try{localStorage.setItem('lang',l)}catch(e){}
    document.querySelectorAll('.MN-lb').forEach(function(b){b.classList.toggle('on',b.dataset.l===l)});
  }
  window.setLang=setLang;
  var path=window.location.pathname.replace(/\\/$/,'').replace(/\\/index\\.html$/,'/');
  document.querySelectorAll('.MN-links a,.MN-mob a').forEach(function(a){
    var h=(a.getAttribute('href')||'').replace(/\\/$/,'').replace(/\\/index\\.html$/,'/');
    if(h&&h===path)a.classList.add('MN-active');
  });
  var burger=document.querySelector('.MN-burger');
  var mob=document.querySelector('.MN-mob');
  if(burger&&mob){
    burger.addEventListener('click',function(){burger.classList.toggle('open');mob.classList.toggle('open')});
    document.addEventListener('click',function(e){if(!e.target.closest('nav')&&!e.target.closest('.MN-mob')){burger.classList.remove('open');mob.classList.remove('open')}});
  }
  try{setLang(localStorage.getItem('lang')||'en')}catch(e){setLang('en')}
})();
</script>"""

# ═══════════════════════════════════
# PLATFORM NAV — 6 link
# Засах бол энд засна
# ═══════════════════════════════════
PLAT_NAV = """<nav class="MN">
  <a href="/" class="MN-logo">research.nexcore.ltd</a>
  <div class="MN-links">
    <a href="/intro.html"><span data-li="en">Intro</span><span data-li="mn">Танилцуулга</span></a>
    <a href="/landscape.html"><span data-li="en">Landscape</span><span data-li="mn">Хүрээ</span></a>
    <a href="/verify.html"><span data-li="en">Verify</span><span data-li="mn">Шалгах</span></a>
    <a href="/roadmap.html"><span data-li="en">Roadmap</span><span data-li="mn">Зам</span></a>
    <a href="/contact.html"><span data-li="en">Contact</span><span data-li="mn">Холбоо</span></a>
    <a href="/paper1/"><span data-li="en">Research #001</span><span data-li="mn">Судалгаа #001</span></a>
  </div>
  <div class="MN-btns">
    <button class="MN-lb" data-l="en" onclick="setLang('en')">ENG</button>
    <button class="MN-lb" data-l="mn" onclick="setLang('mn')">MN</button>
    <button class="MN-burger"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="MN-mob">
  <a href="/intro.html"><span data-li="en">Intro</span><span data-li="mn">Танилцуулга</span></a>
  <a href="/landscape.html"><span data-li="en">Landscape</span><span data-li="mn">Хүрээ</span></a>
  <a href="/verify.html"><span data-li="en">Verify</span><span data-li="mn">Шалгах</span></a>
  <a href="/roadmap.html"><span data-li="en">Roadmap</span><span data-li="mn">Зам</span></a>
  <a href="/contact.html"><span data-li="en">Contact</span><span data-li="mn">Холбоо</span></a>
  <a href="/paper1/"><span data-li="en">Research #001</span><span data-li="mn">Судалгаа #001</span></a>
</div>"""

# ═══════════════════════════════════
# PLATFORM FOOTER
# ═══════════════════════════════════
PLAT_FOOT = """<footer class="MN-foot">
  <span style="flex:1;display:flex;align-items:center;justify-content:center;gap:4px">
    <span data-li="en">Platform · Open archive</span>
    <span data-li="mn">Платформ · Нээлттэй архив</span>
    <span class="MN-foot-sep">·</span>
    <a href="/intro.html"><span data-li="en">Intro</span><span data-li="mn">Танилцуулга</span></a>
    <span class="MN-foot-sep">·</span>
    <a href="/landscape.html"><span data-li="en">Landscape</span><span data-li="mn">Хүрээ</span></a>
    <span class="MN-foot-sep">·</span>
    <a href="/verify.html"><span data-li="en">Verify</span><span data-li="mn">Шалгах</span></a>
    <span class="MN-foot-sep">·</span>
    <a href="/site-map.html">Site Map</a>
  </span>
  <span>v1.0</span>
</footer>"""

# ═══════════════════════════════════
# PAPER1 NAV — 17 link
# Засах бол энд засна
# ═══════════════════════════════════
P1_NAV = """<nav class="MN">
  <a href="/paper1/" class="MN-logo">Results</a>
  <div class="MN-sep"></div>
  <div class="MN-links">
    <a href="/paper1/"><span data-li="en">Results</span><span data-li="mn">Үр дүн</span></a>
    <a href="/paper1/formalism.html"><span data-li="en">Formalism</span><span data-li="mn">Формал</span></a>
    <a href="/paper1/charts.html"><span data-li="en">Charts</span><span data-li="mn">Графикууд</span></a>
    <a href="/paper1/calculator.html"><span data-li="en">Calculator</span><span data-li="mn">Тооцоолол</span></a>
    <a href="/paper1/lab.html"><span data-li="en">Analysis Lab</span><span data-li="mn">Лаб</span></a>
    <a href="/paper1/steven_clark.html">Steven Clark f(x)</a>
    <a href="/paper1/faq.html">FAQ</a>
    <a href="/paper1/methods.html"><span data-li="en">Methods</span><span data-li="mn">Аргачлал</span></a>
    <a href="/paper1/references.html"><span data-li="en">References</span><span data-li="mn">Эшлэл</span></a>
    <a href="/paper1/nulltests.html">Null Tests</a>
    <a href="/paper1/livestats.html">Live Stats</a>
    <a href="/paper1/roadmap.html">Roadmap</a>
    <a href="/paper1/discussion.html">Discussion</a>
    <a href="/paper1/about.html">About</a>
    <a href="/paper1/replication.html"><span data-li="en">Replicate</span><span data-li="mn">Давтах</span></a>
    <a href="/paper1/data.html"><span data-li="en">Data</span><span data-li="mn">Өгөгдөл</span></a>
    <a href="/paper1/changelog.html">Changelog</a>
  </div>
  <div class="MN-sep"></div>
  <a href="/" class="MN-plat">← Platform</a>
  <div class="MN-btns">
    <button class="MN-lb" data-l="en" onclick="setLang('en')">ENG</button>
    <button class="MN-lb" data-l="mn" onclick="setLang('mn')">MN</button>
    <button class="MN-burger"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="MN-mob">
  <a href="/paper1/"><span data-li="en">Results</span><span data-li="mn">Үр дүн</span></a>
  <a href="/paper1/formalism.html"><span data-li="en">Formalism</span><span data-li="mn">Формал</span></a>
  <a href="/paper1/charts.html"><span data-li="en">Charts</span><span data-li="mn">Графикууд</span></a>
  <a href="/paper1/calculator.html"><span data-li="en">Calculator</span><span data-li="mn">Тооцоолол</span></a>
  <a href="/paper1/lab.html">Analysis Lab</a>
  <a href="/paper1/steven_clark.html">Steven Clark f(x)</a>
  <a href="/paper1/faq.html">FAQ</a>
  <a href="/paper1/methods.html"><span data-li="en">Methods</span><span data-li="mn">Аргачлал</span></a>
  <a href="/paper1/references.html"><span data-li="en">References</span><span data-li="mn">Эшлэл</span></a>
  <a href="/paper1/nulltests.html">Null Tests</a>
  <a href="/paper1/livestats.html">Live Stats</a>
  <a href="/paper1/roadmap.html">Roadmap</a>
  <a href="/paper1/discussion.html">Discussion</a>
  <a href="/paper1/about.html">About</a>
  <a href="/paper1/replication.html"><span data-li="en">Replicate</span><span data-li="mn">Давтах</span></a>
  <a href="/paper1/data.html"><span data-li="en">Data</span><span data-li="mn">Өгөгдөл</span></a>
  <a href="/paper1/changelog.html">Changelog</a>
  <hr>
  <a href="/">← Platform</a>
</div>"""

# ═══════════════════════════════════
# PAPER1 FOOTER
# ═══════════════════════════════════
P1_FOOT = """<footer class="MN-foot">
  <span style="flex:1;display:flex;align-items:center;justify-content:center;gap:4px">
    <span data-li="en" style="font-style:italic">Observations only — not a proof of RH</span>
    <span data-li="mn" style="font-style:italic">Тооцооллын ажиглалт — RH нотолгоо биш</span>
    <span class="MN-foot-sep">·</span>
    <a href="/paper1/"><span data-li="en">Results</span><span data-li="mn">Үр дүн</span></a>
    <span class="MN-foot-sep">·</span>
    <a href="/paper1/replication.html"><span data-li="en">Replicate</span><span data-li="mn">Давтах</span></a>
    <span class="MN-foot-sep">·</span>
    <a href="/paper1/data.html"><span data-li="en">Data</span><span data-li="mn">Өгөгдөл</span></a>
    <span class="MN-foot-sep">·</span>
    <a href="/paper1/about.html"><span data-li="en">About</span><span data-li="mn">Тухай</span></a>
    <span class="MN-foot-sep">·</span>
    <a href="https://zenodo.org/records/20077673" target="_blank">DOI</a>
  </span>
  <span>v0.4</span>
</footer>"""

# ═══════════════════════════════════
# ФАЙЛЫН ЖАГСААЛТ
# ═══════════════════════════════════
PLAT_FILES = [
    'contact.html', 'index.html', 'intro.html',
    'landscape.html', 'roadmap.html', 'site-map.html', 'verify.html'
]

P1_FILES = [
    'paper1/about.html', 'paper1/calculator.html', 'paper1/changelog.html',
    'paper1/charts.html', 'paper1/data.html', 'paper1/discussion.html',
    'paper1/faq.html', 'paper1/formalism.html', 'paper1/index.html',
    'paper1/lab.html', 'paper1/livestats.html', 'paper1/methods.html',
    'paper1/nulltests.html', 'paper1/references.html', 'paper1/replication.html',
    'paper1/roadmap.html', 'paper1/steven_clark.html'
]
