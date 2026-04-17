from fastapi import FastAPI
from supabase import create_client, Client
from fastapi.responses import HTMLResponse
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api")
async def root():
    response = supabase.table("president").select("*", count="exact").execute()
    return {
        "message": "Hello World",
        "president_count": response.count
    }
