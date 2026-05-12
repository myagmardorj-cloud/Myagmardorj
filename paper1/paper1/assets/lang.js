// Nexcore Research — shared lang toggle
function setLang(l){
  document.querySelectorAll('[data-li]').forEach(function(e){
    e.style.display = e.dataset.li === l ? '' : 'none';
  });
  document.querySelectorAll('.MN-lb').forEach(function(b){
    b.classList.toggle('MN-active', b.dataset.l === l);
  });
  try { localStorage.setItem('lang', l); } catch(e){}
}
function initLang(){
  var saved = 'en';
  try { saved = localStorage.getItem('lang') || 'en'; } catch(e){}
  setLang(saved);
}
document.addEventListener('DOMContentLoaded', initLang);
