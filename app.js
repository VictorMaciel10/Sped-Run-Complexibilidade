const API = location.origin.replace(/\/$/, "");
let token = null;
let sessionId = null;
let questions = [];
let i = 0;
let t0 = 0;
let totalScore = 0;

function setLog(x){
  document.getElementById('log').textContent =
    (typeof x === 'string') ? x : JSON.stringify(x, null, 2);
}
function setStatus(x){ document.getElementById('status').textContent = x; }
function elapsed(){ return performance.now() - t0; }

// ---------------- AUTH ----------------

async function register(){
  const username = document.getElementById('user').value;
  const password = document.getElementById('pass').value;

  const r = await fetch(`${API}/auth/register`, {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({username,password})
  });

  const j = await r.json();
  if (j.access_token) {
    token = j.access_token;
  }
  setLog(j);
  setStatus('Registrado');
}

async function login(){
  const form = new URLSearchParams();
  form.append('username', document.getElementById('user').value);
  form.append('password', document.getElementById('pass').value);

  const r = await fetch(`${API}/auth/login`, {
    method:'POST',
    headers:{'Content-Type':'application/x-www-form-urlencoded'},
    body:form
  });

  const j = await r.json();
  token = j.access_token;
  setLog(j);
  setStatus('Logado');

  // carrega histórico da última sessão do usuário logado
  await loadLastSession();
}

// ------------- GAME FLOW -------------

async function launch(){
  const r = await fetch(`${API}/game/launch`, {
    method:'POST',
    headers:{'Authorization':`Bearer ${token}`}
  });

  const j = await r.json();
  sessionId = j.session_id;
  questions = j.questions;
  i = 0;
  totalScore = 0;

  document.getElementById('sess').textContent = sessionId;
  document.getElementById('total').textContent = totalScore;

  // esconde painel final se estiver visível
  document.getElementById('final-panel').style.display = 'none';
  document.getElementById('final-details').innerHTML = '';

  setLog(j);
  setStatus('Sessão iniciada');
  renderQuestion();
}

function renderQuestion(){
  const q = questions[i];
  document.getElementById('q-title').textContent = q ? `Q${i+1}. ${q.text}` : 'Fim!';
  const box = document.getElementById('options');
  box.innerHTML = '';

  if(!q){ return; }

  // start timer
  t0 = performance.now();
  const elapsedDom = document.getElementById('elapsed');
  (function tick(){
    elapsedDom.textContent = Math.floor(elapsed());
    if(questions[i]) requestAnimationFrame(tick);
  })();

  q.options.forEach(o => {
    const btn = document.createElement('div');
    btn.className = 'opt';
    btn.textContent = o.text;
    btn.onclick = () => submit(q.id, o.id);
    box.appendChild(btn);
  });
}

async function submit(question_id, option_id){
  const ms = Math.floor(elapsed());

  const r = await fetch(`${API}/game/answer`, {
    method:'POST',
    headers:{
      'Authorization':`Bearer ${token}`,
      'Content-Type':'application/json'
    },
    body: JSON.stringify({
      session_id: sessionId,
      question_id,
      option_id,
      elapsed_ms: ms
    })
  });

  const j = await r.json();
  setLog(j);

  if(j.correct){
    totalScore = j.total_score;
    document.getElementById('total').textContent = totalScore;
    i++;
    renderQuestion();
  } else {
    alert('❌ Resposta incorreta. Tente novamente!');
  }
}

async function finalize(){
  if (!sessionId) return;

  const r = await fetch(`${API}/game/score?session_id=${sessionId}`, {
    method:'POST',
    headers:{'Authorization':`Bearer ${token}`}
  });

  const j = await r.json();
  setLog(j);
  setStatus('Finalizado');

  // --- painel bonitinho ---
  document.getElementById('final-panel').style.display = 'block';
  document.getElementById('final-session-id').textContent = j.session_id;
  document.getElementById('final-score').textContent = j.total_score;

  const totalMs = (j.answers || []).reduce(
    (acc, a) => acc + (a.elapsed_ms || 0),
    0
  );
  document.getElementById('final-time').textContent = totalMs;

  const details = document.getElementById('final-details');
  details.innerHTML = '';

  (j.answers || []).forEach((a, idx) => {
    const row = document.createElement('div');
    row.className = 'answer-row';
    row.innerHTML = `
      <div class="pill">Questão ${idx + 1}</div>
      <div>
        <div>Resposta (option_id): <strong>${a.option_id}</strong></div>
        <div>${a.correct ? '✅ <strong>Alternativa correta</strong>' : '❌ <strong>Alternativa errada</strong>'}</div>
        <div>Tempo para resposta em ms: <strong>${a.elapsed_ms}</strong></div>
        <div>Pontuação atingida: <strong>${a.score_awarded}</strong></div>
      </div>
    `;
      details.appendChild(row);
  });

  // Atualiza também o card "Última sessão"
  await loadLastSession();
}

// ------------- ÚLTIMA SESSÃO -------------

async function loadLastSession(){
  if (!token) return;

  const r = await fetch(`${API}/game/last-session`, {
    method: 'GET',
    headers: { 'Authorization': `Bearer ${token}` }
  });

  // pra debug: mostra no log o retorno desse endpoint
  if (!r.ok) {
    setLog({ endpoint: '/game/last-session', status: r.status });
    return;
  }

  const j = await r.json();

  // também joga no log pra você ver o JSON
  setLog({ endpoint: '/game/last-session', data: j });

  const scoreSpan = document.getElementById('last-score');
  const timeSpan = document.getElementById('last-time');

  if (!j.session_id){
    scoreSpan.textContent = '-';
    timeSpan.textContent = '-';
    return;
  }

  scoreSpan.textContent = j.total_score;
  timeSpan.textContent = j.total_time_ms;
}