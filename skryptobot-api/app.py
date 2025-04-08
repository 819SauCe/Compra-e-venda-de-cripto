import uvicorn
from insert_data import insert_data
from predict_data import fetch_and_store_data
from run_api import app

if __name__ == "__main__":
    insert_data()
    fetch_and_store_data()

    uvicorn.run(app, host="0.0.0.0", port=8000)