
(function(){
  var KEY='wfn-lang', body=document.body, btns=document.querySelectorAll('.langbar button');
  function set(l){
    body.setAttribute('data-lang',l);
    btns.forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-l')===l?'true':'false');});
    document.documentElement.setAttribute('lang', l==='es'?'es':'en');
    try{localStorage.setItem(KEY,l);}catch(e){}
  }
  var start='en';
  try{var m=location.search.match(/lang=(en|es|both)/); if(m){start=m[1];} else {start=localStorage.getItem(KEY)||'en';}}catch(e){}
  btns.forEach(function(b){b.addEventListener('click',function(){set(b.getAttribute('data-l'));});});
  set(start);
})();
