from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}