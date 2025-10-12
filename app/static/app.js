const API = location.origin.replace(/\/$/, "");
let token = null;
let sessionId = null;
let questions = [];
let i = 0;
let t0 = 0;
let totalScore = 0;

function setLog(x){ document.getElementById('log').textContent = (typeof x === 'string')? x : JSON.stringify(x, null, 2); }
function setStatus(x){ document.getElementById('status').textContent = x; }
function elapsed(){ return performance.now() - t0; }

async function register(){
  const username = document.getElementById('user').value; const password = document.getElementById('pass').value;
  const r = await fetch(`${API}/auth/register`, {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({username,password})});
  const j = await r.json(); token = j.access_token; setLog(j); setStatus('Registrado');
}
async function login(){
  const form = new URLSearchParams();
  form.append('username', document.getElementById('user').value);
  form.append('password', document.getElementById('pass').value);
  const r = await fetch(`${API}/auth/login`, {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'}, body:form});
  const j = await r.json(); token = j.access_token; setLog(j); setStatus('Logado');
}

async function launch(){
  const r = await fetch(`${API}/game/launch`, {method:'POST', headers:{'Authorization':`Bearer ${token}`}});
  const j = await r.json(); sessionId = j.session_id; questions = j.questions; i = 0; totalScore = 0;
  document.getElementById('sess').textContent = sessionId; document.getElementById('total').textContent = totalScore; setLog(j); setStatus('Sessão iniciada');
  renderQuestion();
}

function renderQuestion(){
  const q = questions[i];
  document.getElementById('q-title').textContent = q ? `Q${i+1}. ${q.text}` : 'Fim!';
  const box = document.getElementById('options'); box.innerHTML = '';
  if(!q){ return; }
  // start timer
  t0 = performance.now();
  const elapsedDom = document.getElementById('elapsed');
  (function tick(){ elapsedDom.textContent = Math.floor(elapsed()); if(questions[i]) requestAnimationFrame(tick); })();

  q.options.forEach(o => {
    const btn = document.createElement('div');
    btn.className = 'opt';
    btn.textContent = o.text; btn.onclick = () => submit(q.id, o.id);
    box.appendChild(btn);
  })
}

async function submit(question_id, option_id){
  const ms = Math.floor(elapsed());
  const r = await fetch(`${API}/game/answer`, {
    method:'POST',
    headers:{'Authorization':`Bearer ${token}`, 'Content-Type':'application/json'},
    body: JSON.stringify({ session_id: sessionId, question_id, option_id, elapsed_ms: ms })
  });
  const j = await r.json(); setLog(j);
  if(j.correct){ totalScore = j.total_score; document.getElementById('total').textContent = totalScore; i++; renderQuestion(); }
  else { alert('❌ Resposta incorreta. Tente novamente!'); }
}

async function finalize(){
  const r = await fetch(`${API}/game/score?session_id=${sessionId}`, {method:'POST', headers:{'Authorization':`Bearer ${token}`}});
  const j = await r.json(); setLog(j); setStatus('Finalizado');
}