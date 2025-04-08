import asyncio
from insert_data import insert_data
from predict_data import fetch_and_store_data
from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
import os

app = FastAPI()

# Função para inserir dados
async def run_insert_data():
    print("Running insert_data()...")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, insert_data)
    print("Finished insert_data()")

# Função para buscar e armazenar dados
async def run_fetch_and_store_data():
    print("Running fetch_and_store_data()...")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, fetch_and_store_data)
    print("Finished fetch_and_store_data()")

# Função de inicialização
@app.on_event("startup")
async def startup():
    print("Starting the application...")
    # Executar ambas as funções assíncronas
    await asyncio.gather(run_insert_data(), run_fetch_and_store_data())

# Rota para testar
@app.get("/")
async def root():
    return {"message": "Hello World"}
