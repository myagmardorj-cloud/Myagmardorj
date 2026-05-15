from pathlib import Path
import re

p = Path(r"C:\Myagmardorj\paper1\steven_clark.html")

html = p.read_text(encoding="utf-8", errors="ignore")

PAPER_NAV = """
<nav class="MN">
  <a href="/" class="MN-logo">Nexcore Research</a>

  <div class="MN-links">
    <a href="/paper1/">Results</a>
    <a href="/paper1/formalism.html">Formalism</a>

    <span class="MN-more">
      <button onclick="MN_toggle(this)">More ▾</button>

      <div class="MN-dd">
        <a href="/paper1/charts.html">Charts</a>
        <a href="/paper1/calculator.html">Calculator</a>
        <a href="/paper1/lab.html">Analysis Lab</a>
        <a href="/paper1/steven_clark.html">Steven Clark f(x)</a>
        <a href="/paper1/livestats.html">Live Stats</a>
        <a href="/paper1/nulltests.html">Null Tests</a>
        <a href="/paper1/faq.html">FAQ</a>
        <a href="/paper1/methods.html">Methods</a>
        <a href="/paper1/references.html">References</a>
        <a href="/paper1/roadmap.html">Roadmap</a>
        <a href="/paper1/discussion.html">Discussion</a>
        <a href="/paper1/about.html">About</a>
        <a href="/paper1/replication.html">Replicate</a>
        <a href="/paper1/data.html">Data</a>
        <a href="/paper1/changelog.html">Changelog</a>
      </div>
    </span>
  </div>

  <div>
    <button class="MN-lb" data-l="en" onclick="setLang('en')">ENG</button>
    <button class="MN-lb" data-l="mn" onclick="setLang('mn')">МОН</button>
  </div>
</nav>
"""

html = re.sub(
    r"<nav[\s\S]*?</nav>",
    PAPER_NAV,
    html,
    count=1,
    flags=re.I
)

p.write_text(html, encoding="utf-8")

print("steven_clark nav fixed")