// Canonical language system
function setLang(l){
  document.body.classList.remove('en','mn');
  document.body.classList.add(l);
  document.querySelectorAll('.MN-lb,.lb,.MN-active').forEach(function(b){
    if(b.dataset && b.dataset.l){
      b.classList.toggle('MN-active', b.dataset.l === l);
      b.classList.toggle('active', b.dataset.l === l);
    }
  });
  var fl = document.getElementById('faq-list');
  if(fl){ fl.innerHTML=''; setTimeout(function(){ if(typeof initFAQ==='function') initFAQ(); }, 10); }
  localStorage.setItem('lang', l);
}
(function(){ setLang(localStorage.getItem('lang') || 'en'); })();
