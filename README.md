# Sped-Run-Complexibilidade

## Speed Run de Complexidade — Backend (Fase 1)

Backend mínimo em **FastAPI** para o plugin **Speed Run de Complexidade**.  
Este repositório atende aos requisitos da **Fase 1 (início e preparação)**.

---

## Objetivo
- Subir um backend FastAPI com endpoint **/health** respondendo **"ok"**.  
- Fornecer README com **instruções para rodar localmente**.  
- Publicar no **GitHub** com **branching** básico.

---

##  Stack Utilizada
- **Linguagem:** Python 3.10+  
- **Framework Web:** FastAPI  
- **Servidor ASGI:** Uvicorn  

---

## 🗂️ Estrutura inicial do projeto
speedrun-complexidade/
├─ app/
│  ├─ __init__.py
│  └─ routes/            (reservado para rotas futuras)
├─ tests/                (reservado para testes)
├─ main.py               (ponto de entrada FastAPI)
├─ requirements.txt
├─ .gitignore
└─ README.md

---

## Como rodar localmente

1) Clonar o repositório
git clone https://github.com/VictorMaciel10/Sped-Run-Complexibilidade.git
cd Sped-Run-Complexibilidade

2) Criar e ativar o ambiente virtual
Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1
(se o PowerShell bloquear a execução, abra o CMD e use: .\.venv\Scripts\activate.bat)

macOS / Linux (bash/zsh):
python3 -m venv .venv
source .venv/bin/activate

3) Instalar dependências
pip install -r requirements.txt

4) Rodar o servidor FastAPI (Uvicorn)
uvicorn main:app --reload --port 8000
A API ficará acessível em: http://127.0.0.1:8000

5) Testar o endpoint /health
Navegador:
http://127.0.0.1:8000/health

cURL:
curl http://127.0.0.1:8000/health
(Resposta esperada: "ok")

PowerShell:
Invoke-WebRequest http://127.0.0.1:8000/health | Select-Object -ExpandProperty Content

Documentação automática:
Swagger: http://127.0.0.1:8000/docs
Redoc:   http://127.0.0.1:8000/redoc

---

## 👥 Integrantes do grupo
- Victor de Souza Maciel  
- Nathan de Oliveira Gomes  
- Everton Matias Cordeiro de Brito  

---

## 🛠️ Branching sugerido
- main: estável  
- dev: integrações do time  
- features: feature/<nome> (ex.: feature/score-calculator)

Comandos iniciais:
git init
git add .
git commit -m "Fase 1: estrutura mínima + /health ok"
git branch -M main
git remote add origin https://github.com/VictorMaciel10/Sped-Run-Complexibilidade.git
git push -u origin main

Criar branch de desenvolvimento:
git checkout -b dev
git push -u origin dev


