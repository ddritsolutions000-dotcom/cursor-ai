# Backend server using FastAPI for Cursor AI
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to Cursor AI backend server!"}