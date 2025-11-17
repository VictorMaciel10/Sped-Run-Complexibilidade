# Speed Run de Complexidade (⚡🏃)

Joguinho gamificado de perguntas & respostas sobre **Computabilidade e Complexidade**, desenvolvido com FastAPI + SQLModel + SQLite. Ajuda estudantes a praticarem conceitos como Máquinas de Turing, indecidibilidade, RE/R, P vs NP, reduções polinomiais, hierarquia de tempo e EXPTIME. Backend serve a API e a interface simples em `/static/index.html`.


Video de apresentação: https://www.youtube.com/watch?v=d8waiTivDVI
---

# 🔧 Requisitos
- Python 3.11+
- Git
- Windows, Mac ou Linux
- (Opcional) Docker

---

# COMO RODAR O PROJETO (PASSO A PASSO)

## 1) Clonar o repositório
git clone https://github.com/VictorMaciel10/Sped-Run-Complexibilidade.git  
cd Sped-Run-Complexibilidade

## 2) Criar ambiente virtual

### Windows (PowerShell ou CMD):
py -3.11 -m venv .venv  
.\.venv\Scripts\activate

### Windows (Git Bash):
python -m venv .venv  
source .venv/Scripts/activate

### Mac/Linux:
python3 -m venv .venv  
source .venv/bin/activate

## 3) Instalar dependências
pip install -r requirements.txt

## 4) (Opcional) Criar .env
copy .env.example .env  
# cp .env.example .env

Variáveis aceitas:
DATABASE_URL=sqlite:///speedrun.db  
SECRET_KEY=sua_chave_super_secreta  

## 5) Rodar o seed (cria perguntas no banco)
python -m app.seed

Saída esperada:
Perguntas inseridas!

## 6) Subir o servidor  
⚠ Importante: se estiver em pasta do OneDrive, não use reload.  
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000

---

# Jogar o Jogo
Acesse no navegador:  
http://127.0.0.1:8000/static/index.html

Fluxo do usuário:
1. Criar usuário  
2. Fazer login  
3. Clicar em **Launch**  
4. Responder perguntas  
5. Ver pontuação final  

---

# Documentação da API 
http://127.0.0.1:8000/docs

Principais endpoints:
- POST /auth/register  
- POST /auth/login  
- POST /game/start  
- GET /questions/next  
- POST /questions/{id}/answer  
- POST /score/finish  
- GET /sessions/{id}  

---

# Banco de Dados
- SQLite (`speedrun.db`)
- Criado automaticamente
- Tabelas do projeto:
  - usuários  
  - sessões  
  - perguntas  
  - respostas  
  - pontuação  

---

#  O que o jogo ensina
- Máquinas de Turing  
- Problema da Parada  
- Linguagens R e RE  
- Classes P, NP, NP-completo  
- Reduções polinomiais  
- Hierarquia de tempo  
- Complexidade EXPTIME  
- Noções fundamentais de decidibilidade  

---

# Testes recomendados
- Criar usuário novo  
- Logar com senha errada  
- Iniciar sessão  
- Responder correto e errado  
- Verificar score/tempo  
- Finalizar sessão  
- Rodar seed após deletar banco  

---

# Autores
Victor de Souza Maciel 
Everton Matias Cordeiro de Brito
Nathan de Oliveira Gomes
