from fastapi import FastAPI, Request, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, init_db, increment_counter
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

POSTGRES_DB_USER = os.getenv('POSTGRES_DB_USER', 'counter_user')
POSTGRES_DB_PASSWORD = os.getenv('POSTGRES_DB_PASSWORD', 'ThePassw0rD')
POSTGRES_DB_HOST = os.getenv('POSTGRES_DB_HOST', '127.0.0.1')
POSTGRES_DB_PORT = os.getenv('POSTGRES_DB_PORT', '5431')

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

class CounterRequest(BaseModel):
    count: int

class CounterResponse(BaseModel):
    result: int

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = None
    try:
        request.state.db = SessionLocal()  # Используем SessionLocal для получения сессии
        response = await call_next(request)
    finally:
        if hasattr(request.state, "db"):
            request.state.db.close()
    return response

@app.get("/", response_class=HTMLResponse)
def read_count(
    request: Request,
    count: int = Query(0, description="The count value"),
) -> CounterResponse:
    counter_value = increment_counter(request.state.db, count)
    return templates.TemplateResponse("index.html", {"request": request, "count": counter_value})
