
from fastapi import FastAPI

app = FastAPI(title="Speed Run de Complexidade API", version="0.1.0")

@app.get("/health")
def health():
    return "ok"
