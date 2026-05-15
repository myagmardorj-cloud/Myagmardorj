(function(){
  'use strict';

  function normalizePath(path){
    path = (path || '/').split('#')[0].split('?')[0];
    if (path === '/') return '/index.html';
    if (path.endsWith('/')) return path + 'index.html';
    return path;
  }

  function linkPath(a){
    try { return normalizePath(new URL(a.getAttribute('href'), window.location.origin).pathname); }
    catch(e){ return normalizePath(a.getAttribute('href') || ''); }
  }

  window.setLang = function(lang){
    lang = lang === 'mn' ? 'mn' : 'en';
    document.body.classList.remove('en','mn');
    document.body.classList.add(lang);
    document.querySelectorAll('.MN-lb').forEach(function(btn){
      btn.classList.toggle('MN-active', btn.dataset.l === lang);
      btn.setAttribute('aria-pressed', String(btn.dataset.l === lang));
    });
    try { localStorage.setItem('lang', lang); } catch(e) {}
  };

  window.MN_toggle = function(btn){
    var drop = btn && btn.closest ? btn.closest('.MN-drop') : null;
    if (drop) drop.classList.toggle('MN-open');
  };

  function setActiveLinks(){
    var current = normalizePath(window.location.pathname);
    document.querySelectorAll('.MN a[href], .MN-mobile a[href]').forEach(function(a){
      var href = linkPath(a);
      var exact = href === current;
      a.classList.toggle('MN-active', exact);
      if (exact) {
        var drop = a.closest('.MN-drop');
        if (drop) drop.classList.add('MN-active');
      }
    });
  }

  function setupMobile(){
    var burger = document.querySelector('.MN-burger');
    var panel = document.querySelector('.MN-mobile');
    if (!burger || !panel) return;
    burger.setAttribute('type','button');
    burger.setAttribute('aria-expanded','false');
    burger.addEventListener('click', function(){
      var open = !panel.classList.contains('MN-open');
      panel.classList.toggle('MN-open', open);
      burger.classList.toggle('MN-open', open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.classList.toggle('MN-menu-open', open);
    });
    panel.addEventListener('click', function(e){
      if (e.target.closest('a')) {
        panel.classList.remove('MN-open');
        burger.classList.remove('MN-open');
        burger.setAttribute('aria-expanded','false');
        document.body.classList.remove('MN-menu-open');
      }
    });
  }

  function setupDropdownTouch(){
    document.querySelectorAll('.MN-drop > a').forEach(function(trigger){
      trigger.addEventListener('click', function(e){
        if (trigger.getAttribute('href') === '#') e.preventDefault();
        if (window.matchMedia('(hover: none)').matches || trigger.getAttribute('href') === '#') {
          var drop = trigger.closest('.MN-drop');
          if (drop) drop.classList.toggle('MN-open');
        }
      });
    });
    document.addEventListener('click', function(e){
      if (!e.target.closest('.MN-drop')) {
        document.querySelectorAll('.MN-drop.MN-open').forEach(function(d){ d.classList.remove('MN-open'); });
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function(){
    var lang = 'en';
    try { lang = localStorage.getItem('lang') || 'en'; } catch(e) {}
    window.setLang(lang);
    setActiveLinks();
    setupMobile();
    setupDropdownTouch();
  });
})();
