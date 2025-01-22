import pendulum
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from api import *

pool = SimpleConnectionPool(1, 10, user="postgres", password="979838870", host="localhost", database="Cripto")

def insert_cripto_value(cripto, valor):
    tabela = "Cripto"
    conn = pool.getconn()
    cursor = conn.cursor()
    query = f"""
    INSERT INTO {tabela} (cripto, data, hora, valor)
    VALUES (%s, %s, %s, %s)
    """
    data = pendulum.now().format("YYYY-MM-DD")
    hora = pendulum.now().format("HH:mm:ss")
    cursor.execute(query, (cripto, data, hora, valor))
    conn.commit()
    pool.putconn(conn)

def cripto_value(cripto):
    tabela = "Cripto"
    conn = pool.getconn()
    cursor = conn.cursor()
    data = pendulum.now().format("YYYY-MM-DD")
    query = f"SELECT valor FROM {tabela} WHERE data = %s AND cripto = %s"
    cursor.execute(query, (data, cripto))
    valor = cursor.fetchone()
    pool.putconn(conn)
    return valor[0] if valor else None

def get_price_and_store(cripto):
    valor = get_price(cripto)
    insert_cripto_value(cripto, valor)

# Execução principal
while True:
    timer = pendulum.now().format("HH:mm")
    hora = "12:00"
    if hora == "12:00" or hora == "00:00":
        get_price_and_store('BTCUSDT')
        get_price_and_store('ETHUSDT')
        get_price_and_store('BNBUSDT')
        get_price_and_store('ADAUSDT')
        get_price_and_store('SOLUSDT')
        get_price_and_store('XRPUSDT')
        get_price_and_store('DOGEUSDT')
        print("Banco de dados atualizado com sucesso!")
