from __future__ import annotations
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .database import init_db
from .routers import auth_router, game_router

# cria tabelas
init_db()

# objeto FastAPI que o uvicorn vai carregar
app = FastAPI(title="Speed Run de Complexidade")

# CORS liberado para testes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rotas da API
app.include_router(auth_router.router)
app.include_router(game_router.router)

# monta arquivos estáticos (pasta app/static)
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def root():
    # só para indicar o caminho da UI
    return {"open": "/static/index.html"}