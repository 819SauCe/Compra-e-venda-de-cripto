from flask import Flask, jsonify
import requests

app = Flask(__name__)

def obter_taxa_dolar_para_real():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates']['BRL']
    except requests.RequestException as e:
        return None

def get_price(crypto):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={crypto}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return float(response.json()['price'])
    except requests.RequestException as e:
        return f"Erro ao obter preço de {crypto}: {e}"

@app.route('/converter', methods=['GET'])
def converter():
    taxa = obter_taxa_dolar_para_real()
    if taxa is not None:
        return jsonify({'taxa_dolar_para_real': taxa}), 200
    else:
        return jsonify({'error': 'Erro ao obter dados da API'}), 500

@app.route('/preco/<crypto>', methods=['GET'])
def preco_cripto(crypto):
    price = get_price(crypto)
    if isinstance(price, float):
        return jsonify({'preco': price}), 200
    else:
        return jsonify({'error': price}), 500

if __name__ == '__main__':
    app.run(debug=True)
