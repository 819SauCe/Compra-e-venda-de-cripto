from insert__data import insert_data
from predict__data import fetch_and_store_data
from run__api import app

if __name__ == "__main__":
    insert_data()
    fetch_and_store_data()
