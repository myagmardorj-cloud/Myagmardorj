// Shared utilities
function copyCode(btn){
  var pre = btn.nextElementSibling;
  navigator.clipboard.writeText(pre.innerText).then(function(){
    btn.textContent = 'COPIED!';
    setTimeout(function(){ btn.textContent = 'COPY'; }, 2000);
  });
}
function toggleFile(header){
  var body = header.nextElementSibling;
  var toggle = header.querySelector('.file-toggle');
  var open = body.style.display !== 'block';
  body.style.display = open ? 'block' : 'none';
  if(toggle) toggle.classList.toggle('open', open);
}
