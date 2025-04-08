try:
    from fastapi import FastAPI
    from supabase import create_client, Client
    from dotenv import load_dotenv
    import os
except ImportError as e:
    print(f"Error importing modules: {e}")
    os.system('pip install {error.name}')
    exit(1)

load_dotenv()
app = FastAPI()
url = os.getenv("SUPA_BASE_URL")
key = os.getenv("SUPA_BASE_KEY")

@app.get("/")
async def root():
    return {"message": "Hello World"}