try:
    import requests
    import json
    import pendulum
    from supabase import create_client, Client
    from dotenv import load_dotenv
    import os
    import time
except ImportError as e:
    print(f"Error importing modules: {e}")
    os.system(f'pip install {e.name}')
    exit(1)

def main():
    load_dotenv()
    url = os.getenv("SUPA_BASE_URL")
    key = os.getenv("SUPA_BASE_KEY")
    policy = os.getenv("SUPA_BASE_POLICY_CRYPTO")
    supabase = create_client(url, key)
    cripto_and_price = {}
    api_binance = 'https://api.binance.com/api/v3/'
    headers = {'Authorization': f'Bearer {key}', 'X-Supabase-Policy': policy}
    cripto_binance = ['BTCUSDT', 'ETHUSDT', 'USDCUSDT', 'FDUSDUSDT', 'XRPUSDT',
                    'SOLUSDT', 'BNBUSDT', 'ADAUSDT', 'DOGEUSDT', 'ETHUSDT',
                        'SUIUSDT', 'PEPEUSDT', 'TRXUSDT', 'LTCUSDT', 'DOTUSDT']

    while True:
        hora_atual = pendulum.now('UTC').format('HH:mm')
        data_atual = pendulum.now('UTC').format('DD/MM/YYYY')

        if hora_atual in ["00:00", "12:00"]:
            try:
                for crypto in cripto_binance:
                    try:
                        url = api_binance + 'avgPrice?symbol=' + crypto
                        response = requests.get(url)
                        data = json.loads(response.text)
                        price = data['price']
                        cripto_and_price[crypto] = [crypto, price, data_atual]
                        print(cripto_and_price[crypto])
                        time.sleep(2)
                    except requests.exceptions.RequestException as e:
                        print(f'Error fetching data for {crypto}: {e}')
                        continue
                    except json.JSONDecodeError as e:
                        print(f'Error decoding JSON for {crypto}: {e}')
                        continue
                    except KeyError:
                        print(f'Par inválido ou sem preço: {crypto} | Resposta: {data}')
                        continue

                for crypto in cripto_and_price:
                    data = cripto_and_price[crypto]
                    try:
                        supabase.table('Cripto').insert({
                            'cripto_name': data[0],
                            'value': float(data[1]),
                            'date_now': data[2]
                        }).execute()
                        print(f"dado inserido: {data}")
                        time.sleep(2)
                    except Exception as e:
                        print(f'Error inserting data into Supabase: {e}')
                        continue

            except Exception as e:
                print(f'Error in main loop: {e}')
                continue