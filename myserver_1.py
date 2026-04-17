from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

@app.get("/", response_class=HTMLResponse)
def root():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return f.read()
