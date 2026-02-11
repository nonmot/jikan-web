from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import create_db_session_context, reset_db_session_context

from .routers import entries


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_session_context()
    yield
    reset_db_session_context()


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entries.router)


@app.get("/health")
def health():
    return {"status": "ok"}
