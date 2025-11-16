# Speed Run de Complexidade (⚡🏃)

Joguinho de perguntas & respostas sobre Computabilidade e Complexidade, feito com **FastAPI + SQLModel + SQLite**.  
Backend serve a API e a página simples em `/static/index.html`.

Principais rotas:
  GET /questions → lista perguntas
  POST /answer → envia resposta
  …
Variáveis de ambiente:
  DATABASE_URL=…
  SECRET_KEY=…
Porta padrão: 8000

## Requisitos
- **Python 3.11+**
- Windows/Mac/Linux
- (Opcional) Docker

## Como rodar (Windows / Mac / Linux)

> Passo a Passo para utilizar

```bash
# 1) clonar o repositório
git clone https://github.com/VictorMaciel10/Sped-Run-Complexibilidade.git
cd https://github.com/VictorMaciel10/Sped-Run-Complexibilidade.git

# 2) criar e ativar venv
# Windows (PowerShell):
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Mac/Linux:
python3 -m venv .venv
source .venv/bin/activate

# 3) instalar dependências
pip install -r requirements.txt

# 4) (opcional) criar .env a partir do exemplo
# (não é obrigatório pra rodar com SQLite)
copy .env.example .env       # Windows
# cp .env.example .env       # Mac/Linux

# 5) (opcional) resetar/semear perguntas
python -m app.seed

Interface do jogo: http://127.0.0.1:8000/static/index.html

Docs da API (Swagger): http://127.0.0.1:8000/docs

Banco é SQLite (speedrun.db) criado automaticamente na raiz do projeto.
# 6) subir o servidor
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
