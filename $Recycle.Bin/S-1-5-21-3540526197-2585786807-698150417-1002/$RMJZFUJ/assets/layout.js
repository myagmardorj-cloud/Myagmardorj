// НОМИН Холдинг — Shared Layout v2 (nomin.co style)
(function(){
  const ROOT = (function(){
    const d = window.location.pathname.split('/').length - 2;
    return d > 0 ? '../'.repeat(d) : '';
  })();

  // ── UTILITY BAR ──
  const utilBar = `
<div class="util-bar">
  <div class="util-in">
    <div class="util-links">
      <a href="${ROOT}suppliers.html">Нийлүүлэгч</a>
      <a href="${ROOT}careers.html">Ажлын байр</a>
      <a href="${ROOT}news.html">Мэдээ мэдээлэл</a>
      <a href="${ROOT}store-locator.html">Салбар байршил</a>
      <a href="https://procurement.nomin.mn" target="_blank">Худалдан авалт</a>
      <a href="${ROOT}contact.html">Холбоо барих</a>
    </div>
    <div class="util-right">
      <a href="tel:18002888" class="util-phone">📞 1800-2888</a>
      <div class="lang-sw">
        <button class="lang-btn act">МН</button>
        <button class="lang-btn">EN</button>
      </div>
    </div>
  </div>
</div>`;

  // ── HEADER ──
  const header = `
<header id="hdr">
  <div class="hdr">
    <a href="${ROOT}index.html" class="hdr-logo">
      <img src="${ROOT}nomin-logo.svg" alt="НОМИН Холдинг">
    </a>
    <nav>
      <div class="ni">
        <a href="${ROOT}about.html" class="nl" data-path="about">Бидний тухай
          <svg class="chev" viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M1 1l4 4 4-4"/></svg>
        </a>
        <div class="drop">
          <a href="${ROOT}about.html">Танилцуулга</a>
          <a href="${ROOT}mission.html">Бидний зорилго</a>
          <a href="${ROOT}history.html">Түүхэн замнал</a>
          <a href="${ROOT}leadership.html">Удирдлагын баг</a>
          <a href="${ROOT}about.html#why">Биднийг сонгох шалтгаан</a>
          <a href="${ROOT}awards.html">Шагнал, өргөмжлөл</a>
        </div>
      </div>
      <div class="ni">
        <a href="${ROOT}business.html" class="nl" data-path="business">Бизнес
          <svg class="chev" viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M1 1l4 4 4-4"/></svg>
        </a>
        <div class="drop">
          <a href="${ROOT}sector-retail.html">Борлуулалт үйлчилгээ</a>
          <a href="${ROOT}sector-import.html">Импорт / Экспорт</a>
          <a href="${ROOT}sector-finance.html">Санхүү &amp; Даатгал</a>
          <a href="${ROOT}sector-construction.html">Барилга / Үл хөдлөх</a>
          <a href="${ROOT}sector-tech.html">Технологи</a>
          <a href="${ROOT}sector-aviation.html">Агаарын тээвэр</a>
        </div>
      </div>
      <a href="${ROOT}brands.html" class="nl" data-path="brands">Брэнд</a>
      <a href="${ROOT}social.html" class="nl" data-path="social">Нийгмийн хариуцлага</a>
      <a href="${ROOT}suppliers.html" class="nl" data-path="suppliers">Нийлүүлэгч</a>
      <a href="${ROOT}about.html#catalogue" class="nl">Группын танилцуулга</a>
    </nav>
    <div class="hdr-r">
      <button class="btn-srch" onclick="document.getElementById('srch-ov').classList.add('open')" title="Хайх">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      </button>
      <a href="https://shop.nomin.mn" target="_blank" class="btn-eshop">e-shop</a>
    </div>
  </div>
</header>`;

  // ── TICKER ──
  const ticker = `
<div class="ticker">
  <div class="ticker-track">
    <span class="ti">Номин Холдинг — ТОП 100 ААН-д 24 дэх жилдээ</span>
    <span class="ti">6,200+ ажилчид</span>
    <span class="ti">260+ брэнд импортлогч</span>
    <span class="ti">Бонус карт — 800,000+ эзэмшигч</span>
    <span class="ti">E-Shop: shop.nomin.mn</span>
    <span class="ti">1992 оноос хойш — 32+ жил</span>
    <span class="ti">Номин Холдинг — ТОП 100 ААН-д 24 дэх жилдээ</span>
    <span class="ti">6,200+ ажилчид</span>
    <span class="ti">260+ брэнд импортлогч</span>
    <span class="ti">Бонус карт — 800,000+ эзэмшигч</span>
    <span class="ti">E-Shop: shop.nomin.mn</span>
    <span class="ti">1992 оноос хойш — 32+ жил</span>
  </div>
</div>`;

  // ── FOOTER ──
  const footer = `
<footer>
  <div class="container ft-main">
    <div class="ft-grid">
      <div>
        <div class="ft-logo"><img src="${ROOT}nomin-logo.svg" alt="НОМИН Холдинг"></div>
        <p class="ft-desc">1992 оноос хойш Монголын эдийн засгийг тэргүүлж, иргэдэд чанартай бараа, үйлчилгээ хүргэж буй холдинг компани.</p>
        <div class="ft-soc">
          <a href="https://www.facebook.com/NominHoldingOfficial/" class="ft-sb" target="_blank">f</a>
          <a href="https://www.youtube.com/channel/UCR7Sz7SYZAi782AnYuXOWzQ" class="ft-sb" target="_blank">▶</a>
          <a href="#" class="ft-sb">𝕏</a>
        </div>
      </div>
      <div class="ft-col">
        <h4>Бидний Тухай</h4>
        <ul>
          <li><a href="${ROOT}about.html">Танилцуулга</a></li>
          <li><a href="${ROOT}about.html#president">Ерөнхийлөгчийн мэндчилгээ</a></li>
          <li><a href="${ROOT}leadership.html">Захирлууд</a></li>
          <li><a href="${ROOT}history.html">Түүхэн замнал</a></li>
          <li><a href="${ROOT}awards.html">Шагнал, Өргөмжлөл</a></li>
        </ul>
      </div>
      <div class="ft-col">
        <h4>Бидний Бизнес</h4>
        <ul>
          <li><a href="${ROOT}business.html">Бүтэц</a></li>
          <li><a href="${ROOT}sector-retail.html">Борлуулалт</a></li>
          <li><a href="${ROOT}sector-import.html">Импорт / Экспорт</a></li>
          <li><a href="${ROOT}sector-finance.html">Санхүү / Даатгал</a></li>
          <li><a href="${ROOT}sector-construction.html">Барилга / Үл хөдлөх</a></li>
          <li><a href="${ROOT}sector-tech.html">Технологи</a></li>
        </ul>
      </div>
      <div class="ft-col">
        <h4>Холбоо барих</h4>
        <div class="ft-ci"><strong>📍</strong>Номин Юнайтед, Хан-Уул дүүрэг, Чингисийн өргөн чөлөө, УБ 17042</div>
        <div class="ft-ci"><strong>📞</strong><a href="tel:18002888" style="color:inherit">1800-2888</a></div>
        <div class="ft-ci"><strong>🖷</strong>+976 7577-9999</div>
        <div class="ft-ci"><strong>✉️</strong><a href="mailto:nomin@nomin.net" style="color:inherit">nomin@nomin.net</a></div>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="ft-bottom">
      <span class="ft-copy">Copyright © 2025 Nomin Holding. All rights reserved.</span>
      <div class="ft-links">
        <a href="${ROOT}terms.html">Үйлчилгээний нөхцөл</a>
        <a href="${ROOT}privacy.html">Нууцлалын бодлого</a>
        <a href="${ROOT}sitemap.html">Site Index</a>
        <a href="${ROOT}contact.html">Холбоо барих</a>
      </div>
    </div>
  </div>
</footer>`;

  // ── CHATBOT ──
  const chatbot = `
<div class="chat-w">
  <div class="chat-pan" id="chat-pan">
    <div class="chat-h">
      <div class="chat-av">🤖</div>
      <div><div class="chat-nm">Номин Туслах</div><div class="chat-st">Онлайн байна</div></div>
    </div>
    <div class="chat-msgs" id="chat-msgs">
      <div class="msg bot">Сайн байна уу! Номин Холдингийн туслахтай холбогдлоо. Үйлчилгээ, байршил, мэдээллийн талаар асуугаарай.</div>
    </div>
    <div class="chat-inp-row">
      <input class="chat-inp" id="chat-inp" placeholder="Асуулт бичнэ үү...">
      <button class="chat-snd" id="chat-snd">➤</button>
    </div>
  </div>
  <button class="chat-tog" id="chat-tog">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
  </button>
</div>`;

  // ── SEARCH OVERLAY ──
  const searchOverlay = `
<div class="srch-ov" id="srch-ov" onclick="if(event.target===this)this.classList.remove('open')">
  <div class="srch-b">
    <div class="srch-row">
      <span class="s-ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></span>
      <input class="s-inp" id="srch-inp" placeholder="Хайх...">
      <button class="s-cls" onclick="document.getElementById('srch-ov').classList.remove('open')">✕</button>
    </div>
    <div class="srch-tags">
      <button class="stag">Бонус карт</button>
      <button class="stag">E-Shop</button>
      <button class="stag">Карьер</button>
      <button class="stag">Дэлгүүр байршил</button>
      <button class="stag">Century 21</button>
      <button class="stag">Тендер</button>
    </div>
    <div class="srch-hint">Ctrl+K — хайлт нээх &nbsp;/&nbsp; Esc — хаах</div>
  </div>
</div>`;

  // ── INJECT ──
  document.body.insertAdjacentHTML('afterbegin', searchOverlay + chatbot + footer);
  document.body.insertAdjacentHTML('afterbegin', ticker);
  document.body.insertAdjacentHTML('afterbegin', header);
  document.body.insertAdjacentHTML('afterbegin', utilBar);

  // ── ACTIVE NAV LINK ──
  const path = window.location.pathname;
  document.querySelectorAll('nav .nl[data-path]').forEach(link => {
    const p = link.dataset.path;
    if (path.includes(p)) link.classList.add('active');
  });

  // ── HEADER SCROLL SHADOW ──
  window.addEventListener('scroll', () => {
    const h = document.getElementById('hdr');
    if (h) h.classList.toggle('scrolled', window.scrollY > 50);
  });

  // ── CHATBOT LOGIC ──
  const rep = {
    default: 'Уучлаарай. Утсаар холбогдоно уу: 1800-2888',
    холбоо: '📞 1800-2888 | ✉️ nomin@nomin.net | 📍 Хан-Уул дүүрэг',
    байршил: 'Дэлгүүрийн байршлыг store-locator.html хаягаас харна уу.',
    карт: 'Бонус карт: card.nomin.mn — 3-10% хөнгөлөлт',
    ажил: 'Ажлын зар: careers.nomin.mn',
    eshop: 'E-Shop: shop.nomin.mn',
    тендер: 'Тендер: procurement.nomin.mn'
  };
  function sendChat() {
    const inp = document.getElementById('chat-inp');
    const msgs = document.getElementById('chat-msgs');
    const t = inp.value.trim();
    if (!t) return;
    msgs.innerHTML += `<div class="msg user">${t}</div>`;
    inp.value = ''; msgs.scrollTop = msgs.scrollHeight;
    setTimeout(() => {
      const lc = t.toLowerCase(); let r = rep.default;
      for (const [k, v] of Object.entries(rep)) if (lc.includes(k)) { r = v; break; }
      msgs.innerHTML += `<div class="msg bot">${r}</div>`;
      msgs.scrollTop = msgs.scrollHeight;
    }, 600);
  }
  document.addEventListener('click', e => {
    if (e.target.id === 'chat-tog') document.getElementById('chat-pan').classList.toggle('open');
    if (e.target.id === 'chat-snd') sendChat();
  });
  document.addEventListener('keypress', e => {
    if (e.target.id === 'chat-inp' && e.key === 'Enter') sendChat();
  });

  // ── SEARCH KEYBOARD SHORTCUT ──
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') document.getElementById('srch-ov').classList.remove('open');
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      document.getElementById('srch-ov').classList.add('open');
      setTimeout(() => document.getElementById('srch-inp').focus(), 50);
    }
  });
  document.querySelectorAll('.stag').forEach(t => t.addEventListener('click', () => {
    document.getElementById('srch-inp').value = t.textContent;
    document.getElementById('srch-inp').focus();
  }));

})();

// ── LANG BUTTONS (for sub-pages that use layout.js) ──
// The util-bar injected by layout.js should also have 3 lang buttons.
// Override the lang switcher in util bar after injection:
(function patchLang(){
  const sw = document.querySelector('.lang-sw');
  if(!sw) return;
  sw.innerHTML = `
    <button class="lang-btn" data-lang="mn" onclick="if(window.NominI18n)NominI18n.setLang('mn')">МН</button>
    <button class="lang-btn" data-lang="en" onclick="if(window.NominI18n)NominI18n.setLang('en')">EN</button>
    <button class="lang-btn" data-lang="ru" onclick="if(window.NominI18n)NominI18n.setLang('ru')">РУ</button>`;
  // mark active
  const cur = (window.NominI18n && window.NominI18n.current()) || localStorage.getItem('nomin_lang') || 'mn';
  sw.querySelectorAll('.lang-btn').forEach(b=>b.classList.toggle('act',b.dataset.lang===cur));
})();
