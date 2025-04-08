import asyncio
from insert_data import insert_data
from predict_data import fetch_and_store_data

async def run_insert_data():
    print("Running insert_data()...")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, insert_data)
    print("Finished insert_data()")

async def run_fetch_and_store_data():
    print("Running fetch_and_store_data()...")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, fetch_and_store_data)
    print("Finished fetch_and_store_data()")

async def main_1():
    print("Starting the application...")
    await run_insert_data()

async def main_2():
    print("Inserting data...")
    await run_fetch_and_store_data()
    print("Fetching and storing data...")

async def main():
    await asyncio.gather(main_1(), main_2())

if __name__ == "__main__":
    asyncio.run(main())