// Shared nav functions
function MN_close(){
  document.querySelectorAll('.MN-dd').forEach(function(d){ d.classList.remove('open'); });
}
function MN_toggle(btn){
  var dd = btn.nextElementSibling;
  var open = dd.classList.toggle('open');
  btn.classList.toggle('MN-active', open);
}
document.addEventListener('click', function(e){
  if(!e.target.closest('.MN-more')) MN_close();
});
