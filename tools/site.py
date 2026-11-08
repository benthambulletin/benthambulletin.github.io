"""Bentham Bulletin site generator.
Usage: python3 site.py <edition.json>   (see EDITION below for schema)
Writes into ./site/: index.html, YYYY/MM/DD/index.html, archive/index.html, issues.json
"""
import json, os, sys, shutil, datetime

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')

CSS = r"""
@font-face{font-family:'PF';src:url(/assets/fonts/PlayfairDisplay.ttf);font-weight:100 900;font-display:swap}
@font-face{font-family:'PFI';src:url(/assets/fonts/PlayfairDisplay-Italic.ttf);font-weight:100 900;font-style:italic;font-display:swap}
@font-face{font-family:'LO';src:url(/assets/fonts/Lora.ttf);font-weight:100 900;font-display:swap}
@font-face{font-family:'LOI';src:url(/assets/fonts/Lora-Italic.ttf);font-weight:100 900;font-style:italic;font-display:swap}
@font-face{font-family:'AR';src:url(/assets/fonts/Archivo.ttf);font-weight:100 900;font-display:swap}
:root{--paper:#f8eedb;--ink:#24170c;--red:#9c3216;--teal:#2f5e3e;--gold:#cf6f1a;--soft:#664a2c;--rule:#d3b88f}
*{box-sizing:border-box}
html{background:#e2cca8;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);font-family:'LO',Georgia,serif;color:var(--ink);font-size:1.15rem;line-height:1.5;font-weight:480}
.page{max-width:44rem;margin:0 auto;padding:1.2rem 1.1rem 2rem}
a{color:inherit}
.kicker{display:flex;justify-content:space-between;font-family:'AR';font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--soft);font-weight:600;margin-bottom:.4rem}
.hr-thick{height:4px;background:var(--ink)}
.dbl{margin:1.4rem 0 .9rem}.dbl-tight{margin:.7rem 0 .6rem}
.dbl .a,.dbl-tight .a{height:3px;background:var(--ink)}
.dbl .b,.dbl-tight .b{height:1px;background:var(--ink);margin-top:3px}
.the{text-align:center;font-family:'PFI';font-style:italic;font-size:1.3rem;color:var(--red);margin-top:.6rem}
.mast{text-align:center;font-family:'PF';font-weight:800;font-size:clamp(2.4rem,11vw,4.4rem);line-height:.98;margin:0 0 .2rem;letter-spacing:-.02em}
.tag{text-align:center;font-family:'AR';font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:var(--teal);font-weight:600}
.orn{text-align:center;color:var(--gold);font-size:1rem;letter-spacing:.9em;margin:.5rem 0 .4rem}
.dateline{text-align:center;font-family:'AR';font-weight:800;font-size:1.1rem;letter-spacing:.14em;text-transform:uppercase}
.place{text-align:center;font-family:'LOI';font-style:italic;font-size:.95rem;color:var(--soft);margin-top:.2rem}
.tiles{display:flex}
.tile{flex:1;text-align:center;padding:.5rem .2rem;border-right:1px solid var(--rule)}
.tile:last-child{border-right:0}
.tile .v{font-family:'PF';font-weight:800;font-size:clamp(1.4rem,6vw,2.2rem);line-height:1.05}
.tile .k{font-family:'AR';font-weight:700;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);margin-top:.15rem}
.tile.good .v{color:var(--teal)}.tile.urg .v{color:var(--red)}
.plate-wrap{text-align:center;margin:1rem 0 0}
.frame{display:block;position:relative;padding:.6rem;border:2px solid var(--ink)}
.frame img{display:block;width:100%;height:auto}
.tick{position:absolute;width:.9rem;height:.9rem;border:2px solid var(--red)}
.tl{top:-2px;left:-2px;border-right:0;border-bottom:0}.tr{top:-2px;right:-2px;border-left:0;border-bottom:0}
.bl{bottom:-2px;left:-2px;border-right:0;border-top:0}.br{bottom:-2px;right:-2px;border-left:0;border-top:0}
.plate-cap{font-family:'AR';font-size:.68rem;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:.7rem}
.plate-sub{font-family:'LOI';font-style:italic;font-size:1.05rem;color:var(--soft);margin-top:.3rem;line-height:1.4}
.sec{text-align:center;font-family:'AR';font-weight:800;font-size:.95rem;letter-spacing:.3em;text-transform:uppercase;margin:0 0 .9rem;color:var(--red)}
.sec:nth-of-type(even){color:var(--teal)}
.sec .o{color:var(--gold);margin:0 .7rem;letter-spacing:0}
.wx{display:flex;align-items:flex-start;gap:1rem;margin-bottom:.8rem}
.bigtemp{font-family:'PF';font-weight:800;font-size:clamp(3.4rem,17vw,5.2rem);line-height:.82;letter-spacing:-.04em;white-space:nowrap}
.bigtemp sup{font-size:.36em;font-weight:500;vertical-align:top;position:relative;top:.15em}
.wxtext{padding-top:.2rem;font-size:1.05em}
.lede{display:block;font-family:'LOI';font-style:italic;font-size:1.1em;color:var(--soft);margin-bottom:.3rem}
.pnote{font-family:'LO';font-size:1rem;line-height:1.5;color:var(--ink);border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:.7rem .2rem;margin:.2rem 0 1rem}.pnote b{color:var(--red);font-family:'PF'}
.note{border:2px solid var(--teal);color:var(--teal);font-family:'AR';font-weight:700;font-size:.78rem;letter-spacing:.05em;text-transform:uppercase;padding:.45rem .7rem;display:inline-block;margin-bottom:.8rem}
.towns{display:flex;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);margin-bottom:.7rem}
.town{flex:1;text-align:center;padding:.6rem .2rem;border-right:1px solid var(--rule)}
.town:last-child{border-right:0}
.town .n{font-family:'AR';font-weight:800;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--teal)}
.town .t{font-family:'PF';font-weight:700;font-size:1.9rem;margin-top:.15rem}
.town .t sup{font-size:.45em;vertical-align:top;position:relative;top:.2em}
.town .d{font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.1rem}
.line{margin-bottom:.5rem}
.lbl{font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;margin-right:.3rem}
.lbl.r{color:var(--red)}.lbl.t{color:var(--teal)}
.baro-top{display:flex;align-items:center;gap:.9rem;margin-bottom:.4rem;flex-wrap:wrap}
.dial.hi{border-color:var(--red);color:var(--red)}
.dial{border:2px solid var(--teal);color:var(--teal);font-family:'AR';font-weight:700;font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;padding:.4rem .65rem;white-space:nowrap}
.press{font-family:'PF';font-weight:800;font-size:2.3rem;letter-spacing:-.02em}
.trend{font-family:'LOI';font-style:italic;font-size:1.15rem;color:var(--red)}
.baro svg{display:block;width:100%;height:auto;margin:.2rem 0}
.ledger{display:flex;gap:1rem;align-items:center}
.ledger .num{flex:0 0 34%}
.ledger .cap{font-family:'AR';font-weight:700;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);text-align:center}
.ledger .big{font-family:'PF';font-weight:800;font-size:clamp(2.2rem,10vw,3.4rem);color:var(--red);text-align:center;line-height:1.05}
.ledger .txt{flex:1}
.wire{display:flex;gap:.7rem;padding:.55rem 0;border-bottom:1px solid #e3cfac}
.wire:last-child{border-bottom:0}
.wire .num{font-family:'PF';font-weight:800;font-size:1.5rem;color:var(--red);min-width:1.3rem;text-align:right;line-height:1.1}
.wire h3{font-family:'PF';font-weight:800;font-size:1.3rem;margin:0 0 .15rem;line-height:1.2}
.wire p{margin:0;font-size:.98em}
.touch-head{text-align:center;font-family:'PF';font-weight:700;font-size:1.5rem;color:var(--red);margin-bottom:.6rem}
.cards{display:flex;gap:.6rem;margin-top:.6rem}
.card{flex:1;border-top:2px solid var(--ink);padding-top:.35rem;min-width:0}
.card .h{font-family:'AR';font-weight:700;font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;color:var(--red)}
.card .m{font-family:'PF';font-weight:700;font-size:1.05rem;margin-top:.1rem}
.card .s{font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft)}
.qbox{border-left:5px solid var(--gold);padding:.2rem 0 .2rem .8rem}
.fam{border:2px solid var(--gold);padding:.65rem .9rem}
.colo{text-align:center;margin-top:.3rem}
.colo .s{font-family:'LOI';font-style:italic;font-size:.82rem;color:var(--soft);line-height:1.5}
.sig{font-family:'PFI';font-style:italic;font-size:1.8rem;margin:.5rem 0 .2rem}
.nav{display:flex;justify-content:space-between;font-family:'AR';font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin-top:1rem}
.nav a{text-decoration:none;font-weight:700}
.nav a:hover{color:var(--red)}
.strip5{display:flex;border-top:1px solid var(--rule);border-bottom:1px solid var(--ink);margin:.2rem 0 .7rem}
.strip5 div{flex:1;text-align:center;padding:.45rem .1rem;border-right:1px solid var(--rule)}
.strip5 div:last-child{border-right:0}
.strip5 .d{font-family:'AR';font-weight:700;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--soft)}
.strip5 .i{font-size:1.3rem;line-height:1.3;color:var(--red)}
.strip5 .h{font-family:'PF';font-weight:700;font-size:1.15rem}
.strip5 .w{font-family:'LOI';font-style:italic;font-size:.7rem;color:var(--soft)}
.sky{display:flex;gap:1rem;align-items:center;margin-bottom:.6rem}
.sky svg{width:5rem;height:5rem;flex:none}
.stars{margin-top:.4rem}
.star{display:flex;gap:.6rem;padding:.35rem 0;border-bottom:1px solid #e3cfac}
.star:last-child{border-bottom:0}
.star .sg{font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--teal);min-width:4.6rem;padding-top:.3rem}
.star .who{font-family:'LOI';font-style:italic;color:var(--soft);font-size:.85em}
.tbl{width:100%;border-collapse:collapse;font-size:.85em;margin:.5rem 0}
.tbl th{font-family:'AR';font-weight:700;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);text-align:left;border-bottom:1px solid var(--ink);padding:.25rem .3rem}
.tbl td{padding:.3rem .3rem;border-bottom:1px solid #e3cfac}
.tbl td.n{text-align:right;font-family:'AR'}
.tbl tr.us td{font-weight:700;color:var(--red)}
.cal{list-style:none;padding:0;margin:.4rem 0 0}
.cal li{display:flex;gap:.7rem;padding:.25rem 0}
.cal .dt{font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--red);min-width:4.2rem;padding-top:.3rem}
.ballot{border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);padding:.5rem 0;font-family:'AR';font-weight:700;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;text-align:center}
.ballot b{color:var(--red)}
.ask{font-family:'LOI';font-style:italic;color:var(--teal);font-size:.95em;margin-top:.5rem}
@media (max-width:480px){
 .kicker{font-size:.58rem;letter-spacing:.12em}
 .sec{letter-spacing:.18em;font-size:.85rem;margin:1.9rem 0 .9rem;padding-top:1.1rem;border-top:1px solid var(--rule)}
.sec:first-of-type{border-top:none}
 .sec .o{margin:0 .4rem}
 .tile .k{font-size:.55rem;letter-spacing:.08em}
 .cards{flex-direction:column;gap:.4rem}
 .card{display:flex;align-items:baseline;gap:.5rem;flex-wrap:wrap;border-top:1px solid var(--rule);padding-top:.3rem}
 .card .h{min-width:100%}
}
.ribbon{display:flex;height:5px;margin:.5rem 0 .9rem;border:1px solid var(--rule)}
.ribbon span{flex:1}
.ribbon span:nth-child(1){background:#9b1c28}
.ribbon span:nth-child(2){background:#fbf5e4}
.ribbon span:nth-child(3){background:#1b3a6b}
.memorial{margin:.9rem 0 1.1rem;text-align:center}
.memorial svg{width:100%;display:block;border:1px solid var(--ink)}
.memorial .mcap{font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.18em;text-transform:uppercase;color:var(--red);margin-top:.45rem}
.memorial .msub{font-family:'LOI';font-style:italic;color:var(--soft);font-size:1rem;margin-top:.25rem}
.board{margin:.9rem 0 1.1rem;text-align:center}
.board svg{width:100%;display:block;border:1px solid var(--ink)}
.alert{background:var(--red);color:#fff;font-family:'AR';font-weight:700;font-size:.8rem;letter-spacing:.04em;padding:.55rem .75rem;margin:0 0 1rem;line-height:1.4}
.alert b{color:#fff}
/* album */
.alb{display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;margin:.6rem 0}
.alb a{display:block;position:relative;line-height:0}
.alb img{width:100%;aspect-ratio:4/3;object-fit:cover;border:1px solid var(--ink)}
.albfig{margin:0 0 1.6rem}
.albfig img{width:100%;border:1px solid var(--ink)}
.albfig .c{font-family:'LOI';font-style:italic;color:var(--soft);font-size:1rem;margin-top:.35rem}
.albfig .d{font-family:'AR';font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;color:var(--red);margin-top:.3rem}
.albfig .d a{color:var(--red);text-decoration:none}
.promo{border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:.6rem .2rem;margin:.9rem 0;text-align:center}
.promo .h{font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;color:var(--red)}
.promo .t{font-family:'LO';font-size:.98rem;line-height:1.45;margin-top:.25rem}
.promo a{color:var(--teal);font-weight:700;text-decoration:none}
/* reader tools: read aloud + bigger print (Garret, Oct 21: for the older readers) */
.tools{display:flex;justify-content:flex-end;gap:.5rem;margin:0 0 .7rem}
.tools button{font-family:'AR';font-weight:700;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);background:transparent;border:2px solid var(--teal);padding:.45rem .7rem;cursor:pointer;line-height:1.2}
.tools button[aria-pressed="true"]{background:var(--teal);color:var(--paper)}
html.big{font-size:125%}
.page a{overflow-wrap:anywhere}
html.big .tools button{font-size:.62rem}
/* archive */
.arch{list-style:none;padding:0;margin:0}
.arch li{display:flex;gap:.9rem;align-items:center;padding:.7rem 0;border-bottom:1px solid #e3cfac}
.arch img{width:6rem;height:4rem;object-fit:cover;border:1px solid var(--ink);flex:none}
.arch a{text-decoration:none}
.arch .d{font-family:'PF';font-weight:700;font-size:1.1rem}
.arch .no{font-family:'AR';font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--soft)}
.arch .c{font-family:'LOI';font-style:italic;color:var(--soft);font-size:.95rem}

.calline{font-family:'AR';font-size:.72rem;letter-spacing:.06em;text-align:center;color:var(--soft);border-bottom:1px solid var(--rule);padding:.45rem .2rem;margin:.2rem 0 .6rem}.calline b{color:var(--red);letter-spacing:.16em;text-transform:uppercase;margin-right:.4rem}
.colo .ask{font-size:.85em;margin:.4rem 0}
.tools.under{justify-content:center;margin:.6rem 0 .2rem}
/* Nov 6: highlight the reader tools for a week (toned down) */
.tools.promo{flex-direction:column;align-items:flex-end;gap:.3rem;margin:0 0 .7rem}
.tools.promo .pr{display:flex;gap:.5rem}
.tools.promo .ph{display:none}
.tools.promo .pt,.tools.promo .home{font-family:'LOI';font-style:italic;font-size:.74rem;color:var(--soft);text-align:right;line-height:1.3}
/* Nov 6: riddle reveal, radar */
.reveal{font-family:'AR';font-weight:700;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--paper);background:var(--teal);border:0;padding:.5rem .8rem;margin-top:.5rem;cursor:pointer}
.qans[hidden]{display:none}
.qans{display:block;font-family:'PF';font-style:italic;font-size:1.25rem;color:var(--red);margin-top:.5rem}
.radar{margin:.6rem 0;border:1px solid var(--rule)}
.radar summary{font-family:'AR';font-weight:700;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--teal);padding:.55rem .7rem;cursor:pointer}
.radar img{display:block;width:100%;height:auto}
.radar .rc{font-family:'LOI';font-style:italic;font-size:.75rem;color:var(--soft);padding:.3rem .6rem .5rem}
.tools.promo .home{font-family:'AR';font-size:.68rem;letter-spacing:.06em;color:var(--teal);text-align:center}
/* Nov 6 layout pass (Garret: "do them all") */
.lbl{white-space:nowrap}
.town .d{font-size:.74rem;line-height:1.25}
.sky svg{border-radius:50%;box-shadow:0 0 0 2px var(--ink)}
.sky svg circle:first-of-type{fill:#5a4d3b}
.touch-head{font-family:'AR';font-weight:800;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);text-align:center;margin:.1rem 0 .6rem}
.inside{display:flex;flex-wrap:wrap;justify-content:center;gap:.2rem .9rem;font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);padding:.5rem .2rem;margin:.9rem 0 .2rem}
.inside span{color:var(--gold);letter-spacing:.2em}
.inside a{color:var(--ink);text-decoration:none;white-space:nowrap}
.inside a:hover{color:var(--red)}
.sec{scroll-margin-top:1rem}
.wire.lead{display:block;border-bottom:2px solid var(--ink);padding:.3rem 0 .9rem;margin-bottom:.4rem}
.wire.lead .num{display:none}
.wire.lead .kick{display:block;font-family:'AR';font-weight:800;font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;color:var(--red);margin-bottom:.25rem}
.wire.lead h3{font-size:1.85rem;line-height:1.12;margin-bottom:.45rem}
.wire.lead p{font-size:1.04em;margin-bottom:.5rem}
.wire.lead p:first-of-type::first-letter{float:left;font-family:'PF';font-weight:800;font-size:3.3em;line-height:.8;padding:.08em .1em 0 0;color:var(--red)}
.pull{font-family:'PF';font-style:italic;font-size:1.25rem;line-height:1.3;text-align:center;color:var(--red);border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:.6rem .4rem;margin:.6rem 1rem}
"""

import hashlib
TOOLS = """<div class="tools"><button type="button" id="bb-read" aria-pressed="false">&#128251; Play the newscast</button><button type="button" id="bb-big" aria-pressed="false">A+ Bigger print</button></div>"""
TOOLS_JS = r"""<script>
(function(){
var root=document.documentElement, big=document.getElementById('bb-big'), rd=document.getElementById('bb-read');
function setBig(on){root.classList.toggle('big',on);big.setAttribute('aria-pressed',on?'true':'false');big.innerHTML=on?'A&minus; Normal print':'A+ Bigger print';try{localStorage.setItem('bb-big',on?'1':'0')}catch(e){}}
try{if(localStorage.getItem('bb-big')==='1')setBig(true)}catch(e){}
big.addEventListener('click',function(){setBig(!root.classList.contains('big'))});
var ss=(window.speechSynthesis&&window.SpeechSynthesisUtterance)?window.speechSynthesis:null; if(!ss&&!rd.getAttribute('data-audio')){rd.style.display='none';return}
function lines(){
  var page=document.querySelector('.page'), c=page.cloneNode(true);
  c.querySelectorAll('.tools,.nav,.kicker,svg,script,img,.sig,.orn').forEach(function(e){e.remove()});
  var box=document.createElement('div'); box.style.cssText='position:absolute;left:-9999px;top:0;width:40rem';
  box.appendChild(c); document.body.appendChild(box);
  var t=c.innerText; box.remove();
  return t.split(/\n+/).map(function(l){return l
    .replace(/(\d)″/g,'$1 inches').replace(/°/g,' degrees').replace(/[·—|]/g,', ')
    .replace(/–/g,' to ').replace(/(\d)a\b/g,'$1 a.m.').replace(/(\d)p\b/g,'$1 p.m.')
    .replace(/[^\x20-\x7E\u00C0-\u024F\u2018-\u201D\u00BD]/g,' ').replace(/\s+/g,' ').trim();})
    .map(function(l){return (l===l.toUpperCase()&&/[A-Z]{3}/.test(l))?l.charAt(0)+l.slice(1).toLowerCase():l})
    .filter(function(l){return /[A-Za-z0-9]/.test(l)});
}
var Q=[],qi=0,on=false,best=null;
// Prefer the phone's best English voice: Premium/Enhanced downloads first, then known natural ones,
// then any US English, then any English.
function pickVoice(){
  if(best)return best;
  var V=(ss.getVoices()||[]).filter(function(x){return /^en/i.test(x.lang)}); if(!V.length)return null;
  function score(x){var n=x.name, s=0;
    if(/premium/i.test(n))s+=100; else if(/enhanced|neural|natural/i.test(n))s+=60;
    if(/^(Ava|Zoe|Evan|Nathan|Noelle|Allison|Susan|Tom|Samantha|Joelle|Aaron)\b/.test(n))s+=20;
    if(/Google US English|Microsoft (Aria|Jenny|Guy)/.test(n))s+=40;
    if(/^en(-|_)US/i.test(x.lang))s+=10;
    if(/Fred|Albert|Bad News|Bahh|Bells|Boing|Bubbles|Cellos|Good News|Jester|Organ|Superstar|Trinoids|Whisper|Wobble|Zarvox|Junior|Ralph|Kathy|Grandma|Grandpa|Rocko|Shelley|Flo|Eddy|Reed|Sandy/.test(n))s-=200;
    return s}
  V.sort(function(a,b){return score(b)-score(a)}); best=V[0]; return best;
}
if(ss&&ss.onvoiceschanged!==undefined)ss.onvoiceschanged=function(){best=null};
if(ss)ss.getVoices();
function stop(){on=false;Q=[];if(ss)ss.cancel();rd.setAttribute('aria-pressed','false');rd.innerHTML='&#128251; Play the newscast'}
function next(){
  if(!on)return; if(qi>=Q.length){stop();return}
  var u=new SpeechSynthesisUtterance(Q[qi++]); u.rate=0.95; u.lang='en-US';
  var v=pickVoice(); if(v){try{u.voice=v}catch(e){}}
  u.onend=next; u.onerror=next; ss.speak(u);
}
var A=null,noAudio=false;
(function(){var u=rd.getAttribute('data-audio'); if(!u){noAudio=true;return}
  try{fetch(u,{method:'HEAD',cache:'no-store'}).then(function(r){if(!r.ok)noAudio=true}).catch(function(){noAudio=true})}catch(e){noAudio=true}})();
function stopAll(){ if(A){try{A.pause()}catch(e){} A=null} stop(); }
function speak(){
  Q=lines(); qi=0; if(!Q.length)return;
  on=true; rd.setAttribute('aria-pressed','true'); rd.innerHTML='&#9632; Stop reading';
  // iPhone: speak inside the tap itself, one line at a time
  if(ss.paused)ss.resume();
  next();
}
rd.addEventListener('click',function(){
  if(on||A){stopAll();return}
  var url=rd.getAttribute('data-audio');
  // First choice: the recorded edition (same natural voice on every phone, nothing to download).
  if(url&&!noAudio){
    A=new Audio(url); A.preload='auto';
    rd.setAttribute('aria-pressed','true'); rd.innerHTML='&#9632; Stop reading';
    A.addEventListener('ended',stopAll);
    A.addEventListener('error',function(){ A=null; noAudio=true; if(!on){ stop(); if(ss)speak(); } });
    var p=A.play(); if(p&&p.catch)p.catch(function(){ if(!A)return; A=null; noAudio=true; stop(); if(ss)speak(); });
    return;
  }
  if(ss)speak();
});
window.addEventListener('pagehide',function(){stopAll()});
})();
</script>"""

PROMO_UNTIL = "2026-11-13"  # Garret, Nov 6: highlight the reader tools for a week


def promo_tools(t):
    """Wrap the two reader buttons in a bigger, explained box for the promo week."""
    btns = t[t.index('<button'):t.rindex('</button>') + len('</button>')]
    return ('<div class="tools promo"><div class="ph">New: two buttons to make the paper easier</div>'
            '<div class="pr">' + btns + '</div>'
            '<div class="pt">New: hear the paper read aloud, or make the print bigger.</div>'
            '<div class="home">Add it to your home screen: Share &rarr; Add to Home Screen.</div></div>')


def place_tools(body, t):
    """Garret, Nov 6: the reader buttons sit centered under the masthead, after the dateline/place line."""
    t = t.replace('<div class="tools">', '<div class="tools under">')
    i = body.find('<div class="place">')
    if i >= 0:
        j = body.find('</div>', i) + len('</div>')
        return body[:j] + '\n' + t + body[j:]
    return t + body


def shell(title, body, og_image=None, desc="A daily almanac for the family", tools=False, audio=None, date=None):
    CSSV = hashlib.md5(CSS.encode()).hexdigest()[:8]
    og = f'<meta property="og:image" content="https://benthambulletin.github.io{og_image}">' if og_image else ''
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">{og}
<meta property="og:type" content="article">
<link rel="stylesheet" href="/assets/style.css?v={CSSV}">
<link rel="icon" href="/assets/favicon.svg">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Bulletin"><meta name="theme-color" content="#24170c"></head><body><div class="page">
{place_tools(body, (TOOLS.replace('id="bb-read"', f'id="bb-read" data-audio="{audio}"') if audio else TOOLS)) if tools else body}
</div>{TOOLS_JS if tools else ""}</body></html>"""

SHORT = {'Family Today': 'Family', 'The Weather Glass': 'Weather', 'The Almanac Sky': 'Sky', 'The Ledger': 'Ledger',
         'The National Wire': 'Nation', 'The Home Wire': 'Home', 'The Marquee': 'Marquee', 'The Gridiron': 'Gridiron',
         'The Chase': 'Chase', 'On This Day': 'On This Day', 'Question of the Day': 'Riddle', 'The Sunday Spotlight': 'Spotlight',
         'The Week Ahead': 'Week Ahead', 'The Sunday Question': 'Sunday Q'}


RADAR = ('<div class="radar"><img loading="lazy" src="https://radar.weather.gov/ridge/standard/KBUF_loop.gif" '
         'alt="National Weather Service radar loop for Buffalo"><div class="rc">Live radar: National Weather Service, Buffalo, the last hour in motion. Refreshes every 5 minutes.</div></div>\n'
         '<script>setInterval(function(){var i=document.querySelector(".radar img");if(i)i.src=i.src.split("?")[0]+"?t="+Date.now()},300000)</script>\n')


def add_radar(body):
    """Garret, Nov 6: the radar runs every day, always open, right under the five-day strip."""
    import re as _re
    body = _re.sub(r'<details class="radar">.*?</details>\n?', '', body, flags=_re.S)
    if 'class="radar"' in body:
        return body
    i = body.find('<div class="strip5">')
    if i < 0:
        return body
    j = body.find('</div>\n</div>', i)
    if j < 0:
        return body
    j += len('</div>\n</div>\n')
    return body[:j] + RADAR + body[j:]


def riddle_reveal(body):
    """Nov 6: the riddle answer hides behind a tap instead of sitting below the fold."""
    import re as _re
    m = _re.search(r'<b>Question of the Day:</b>\s*(.*?)</', body)
    k = body.find('<i>Answer below the fold.</i>')          # the riddle, not the Sunday Question
    q = body.rfind('<div class="qotd">', 0, k) if k >= 0 else body.rfind('<div class="qotd">')
    if not m or q < 0 or 'class="reveal"' in body:
        return body
    ans = m.group(1).strip()
    end = body.find('</div>', q)
    block = body[q:end]
    block2 = _re.sub(r'\s*<i>Answer below the fold\.</i>', '', block)
    btn = ('<br><button type="button" class="reveal" onclick="this.style.display=\'none\';this.nextElementSibling.hidden=false">'
           'Tap for the answer</button><span class="qans" hidden>' + ans + '</span>')
    body = body[:q] + block2 + btn + body[end:]
    return _re.sub(r'<div class="s" style="margin-bottom:8px"><b>Question of the Day:</b>.*?</div>\n?', '', body, count=1)


def inside_today(body):
    """Nov 6: give each section head an id and put an 'Inside today' jump strip under the cover."""
    import re as _re
    if 'class="inside"' in body:
        return body
    links = []
    def tag(m):
        name = _re.sub(r'<[^>]+>', '', m.group(2)).replace('&middot;', '·').strip()
        name = _re.sub(r'^[^A-Za-z]+|[^A-Za-z]+$', '', _re.sub(r'&#?\w+;', '', name)).strip()
        sid = 's-' + _re.sub(r'[^a-z]+', '-', name.lower()).strip('-')
        short = next((v for k, v in SHORT.items() if name.startswith(k)), None)
        if short and sid not in [l[0] for l in links]:
            links.append((sid, short))
        return f'<h2 class="sec" id="{sid}">{m.group(2)}</h2>'
    body = _re.sub(r'<h2 class="sec"( id="[^"]*")?>(.*?)</h2>', tag, body)
    if len(links) < 4:
        return body
    strip = '<nav class="inside" aria-label="Inside today"><span>Inside</span>' + ''.join(f'<a href="#{a}">{b}</a>' for a, b in links) + '</nav>\n'
    i = body.find('<div class="plate-wrap">')
    if i >= 0:
        j = body.find('<div class="plate-sub">', i); j = body.find('</div></div>', j)
        if j > 0:
            j += len('</div></div>')
            return body[:j] + '\n' + strip + body[j:]
    i = body.find('<div class="tiles">')
    if i >= 0:
        j = body.find('</div>\n</div>', i)
        if j > 0:
            j += len('</div>\n</div>')
            return body[:j] + '\n' + strip + body[j:]
    return body


def build(edition):
    """edition: dict with keys date (YYYY-MM-DD), no, body_html (the paper from kicker to colophon,
    with <img src="__PLATE__">), plate_path (jpg on disk), plate_caption, headline."""
    d = datetime.date.fromisoformat(edition['date'])
    slug = d.strftime('%Y/%m/%d')
    outdir = os.path.join(SITE, slug); os.makedirs(outdir, exist_ok=True)
    os.makedirs(os.path.join(SITE, 'assets'), exist_ok=True)
    os.makedirs(os.path.join(SITE, 'archive'), exist_ok=True)
    open(os.path.join(SITE,'assets','style.css'),'w').write(CSS)
    plate_rel = f'/{slug}/plate.jpg'
    if edition.get('plate_path'): shutil.copy(edition['plate_path'], os.path.join(outdir,'plate.jpg'))
    # manifest
    mpath = os.path.join(SITE,'issues.json')
    issues = json.load(open(mpath)) if os.path.exists(mpath) else []
    issues = [i for i in issues if i['date'] != edition['date']]
    entry = {'date':edition['date'],'no':edition['no'],'slug':slug,
             'caption':edition['plate_caption'],'headline':edition['headline']}
    if edition.get('plate_path'): entry['plate'] = plate_rel
    issues.append(entry)
    issues.sort(key=lambda i:i['date'], reverse=True)
    json.dump(issues, open(mpath,'w'), indent=1)
    # prev/next nav
    idx = [i['date'] for i in issues].index(edition['date'])
    newer = issues[idx-1] if idx>0 else None
    older = issues[idx+1] if idx+1 < len(issues) else None
    nav = '<div class="nav">'
    dname = lambda i: datetime.date.fromisoformat(i["date"]).strftime('%A')
    nav += f'<a href="/{older["slug"]}/">&larr; {dname(older)}</a>' if older else '<span></span>'
    nav += '<a href="/album/">Album</a><a href="/archive/">Archive</a>'
    nav += f'<a href="/{newer["slug"]}/">{dname(newer)} &rarr;</a>' if newer else '<a href="/">Today</a>'
    nav += '</div>'
    edition = dict(edition); edition['body_html'] = add_radar(riddle_reveal(inside_today(edition['body_html'])))
    if edition.get('plate_path'):
        pv = hashlib.md5(open(edition['plate_path'],'rb').read()).hexdigest()[:8]
        body = edition['body_html'].replace('__PLATE__', plate_rel+'?v='+pv) + nav
    else:
        body = edition['body_html'] + nav
    title = f"The Bentham Bulletin · No. {edition['no']} · {d.strftime('%A, %B %-d, %Y')}"
    html = shell(title, body, plate_rel, edition['headline'], tools=True, audio=f"/audio/{edition['date']}.mp3", date=edition['date'])
    open(os.path.join(outdir,'index.html'),'w').write(html)
    # front page = newest issue
    newest = issues[0]
    if newest['date'] == edition['date']:
        open(os.path.join(SITE,'index.html'),'w').write(html)
    # archive
    def _thumb(i):
        return f'<img src="{i["plate"]}" alt="">' if i.get('plate') else ''
    items = ''.join(
        f'<li><a href="/{i["slug"]}/">{_thumb(i)}</a><div>'
        f'<div class="no">Vol. I &middot; No. {i["no"]}</div>'
        f'<a href="/{i["slug"]}/"><div class="d">{datetime.date.fromisoformat(i["date"]).strftime("%A, %B %-d, %Y")}</div></a>'
        f'<div class="c">{i["caption"]}</div></div></li>' for i in issues)
    abody = f"""<div class="kicker"><span>The Bentham Bulletin</span><span>Back Issues</span></div>
<div class="hr-thick"></div>
<div class="the">The</div><h1 class="mast">Archive</h1>
<div class="tag">Every edition, newest first</div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<ul class="arch">{items}</ul>
<div class="nav"><span></span><a href="/">Today's paper &rarr;</a></div>"""
    open(os.path.join(SITE,'archive','index.html'),'w').write(shell('The Bentham Bulletin · Archive', abody))
    # album
    os.makedirs(os.path.join(SITE,'album'), exist_ok=True)
    covers = [i for i in issues if i.get('plate')]
    thumbs = ''.join(f'<a href="#p{i["no"]}"><img src="{i["plate"]}" alt="{i["caption"]}"></a>' for i in covers)
    figs = ''.join(
        f'<figure class="albfig" id="p{i["no"]}"><img src="{i["plate"]}" alt="{i["caption"]}">'
        f'<div class="c">{i["caption"]}</div>'
        f'<div class="d"><a href="/{i["slug"]}/">No. {i["no"]} &middot; '
        f'{datetime.date.fromisoformat(i["date"]).strftime("%B %-d, %Y")} &rarr;</a></div></figure>' for i in covers)
    albbody = f"""<div class="kicker"><span>The Bentham Bulletin</span><span>{len(covers)} Covers</span></div>
<div class="hr-thick"></div>
<div class="the">The</div><h1 class="mast">Family Album</h1>
<div class="tag">Every cover, newest first</div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<div class="alb">{thumbs}</div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
{figs}
<div class="nav"><a href="/archive/">&larr; Archive</a><span></span><a href="/">Today's paper &rarr;</a></div>"""
    open(os.path.join(SITE,'album','index.html'),'w').write(shell('The Bentham Bulletin · The Family Album', albbody, covers[0]['plate']))
    open(os.path.join(SITE,'assets','favicon.svg'),'w').write(
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#f5e9bc"/>'
      '<text x="32" y="46" font-family="Georgia,serif" font-weight="700" font-size="40" text-anchor="middle" fill="#c8302f">B</text></svg>')
    return slug

if __name__ == '__main__':
    ed = json.load(open(sys.argv[1]))
    print(build(ed))
