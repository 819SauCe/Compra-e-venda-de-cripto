import time
import threading
import os
from api import obter_taxa_dolar_para_real, get_price
from config import lucro_btc, wallet, take_value, explosion, lucro, take_value_btc, take_value_eth, take_value_bnb, take_value_ada, take_value_sol, take_value_xrp, take_value_doge, take_value_dot, take_value_ltc, take_value_link
# Variáveis de cada cripto
btc_owned = 0.0
btc_purchase_price = 0.0
eth_owned = 0.0
eth_purchase_price = 0.0
bnb_owned = 0.0
bnb_purchase_price = 0.0
ada_owned = 0.0
ada_purchase_price = 0.0
sol_owned = 0.0
sol_purchase_price = 0.0
xrp_owned = 0.0
xrp_purchase_price = 0.0
doge_owned = 0.0
doge_purchase_price = 0.0
dot_owned = 0.0
dot_purchase_price = 0.0
ltc_owned = 0.0
ltc_purchase_price = 0.0
link_owned = 0.0
link_purchase_price = 0.0

btc_info = "Bitcoin: Digital gold, limited supply of 21 million."
eth_info = "Ethereum: Smart contracts platform, second-largest by market cap."
bnb_info = "Binance Coin: Utility token for the Binance exchange."
ada_info = "Cardano: Proof-of-stake blockchain platform for smart contracts."
sol_info = "Solana: High-performance blockchain for decentralized apps."
xrp_info = "Ripple: Digital payment protocol and cryptocurrency."
doge_info = "Dogecoin: Originally created as a meme, now a popular cryptocurrency."

# Evento para controlar a pausa
pausar_evento = threading.Event()

# Funções de venda
def vender_btc():
    global wallet, btc_owned, btc_purchase_price
    if btc_owned > 0:
        btc_usdt = get_price('BTCUSDT')
        valor_venda = btc_owned * btc_usdt
        valor_venda = round(valor_venda, 2)  # Arredondar para 2 casas decimais
        wallet += valor_venda
        print(f"Bitcoin vendido por: {valor_venda:.2f} USDT")
        btc_owned = 0
        btc_purchase_price = 0.0

def vender_eth():
    global wallet, eth_owned, eth_purchase_price
    if eth_owned > 0:
        eth_usdt = get_price('ETHUSDT')
        valor_venda = eth_owned * eth_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"Ethereum vendido por: {valor_venda:.2f} USDT")
        eth_owned = 0
        eth_purchase_price = 0.0

def vender_bnb():
    global wallet, bnb_owned, bnb_purchase_price
    if bnb_owned > 0:
        bnb_usdt = get_price('BNBUSDT')
        valor_venda = bnb_owned * bnb_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"BNB vendido por: {valor_venda:.2f} USDT")
        bnb_owned = 0
        bnb_purchase_price = 0.0

def vender_ada():
    global wallet, ada_owned, ada_purchase_price
    if ada_owned > 0:
        ada_usdt = get_price('ADAUSDT')
        valor_venda = ada_owned * ada_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"ADA vendido por: {valor_venda:.2f} USDT")
        ada_owned = 0
        ada_purchase_price = 0.0

def vender_sol():
    global wallet, sol_owned, sol_purchase_price
    if sol_owned > 0:
        sol_usdt = get_price('SOLUSDT')
        valor_venda = sol_owned * sol_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"SOL vendido por: {valor_venda:.2f} USDT")
        sol_owned = 0
        sol_purchase_price = 0.0

def vender_xrp():
    global wallet, xrp_owned, xrp_purchase_price
    if xrp_owned > 0:
        xrp_usdt = get_price('XRPUSDT')
        valor_venda = xrp_owned * xrp_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"XRP vendido por: {valor_venda:.2f} USDT")
        xrp_owned = 0
        xrp_purchase_price = 0.0

def vender_doge():
    global wallet, doge_owned, doge_purchase_price
    if doge_owned > 0:
        doge_usdt = get_price('DOGEUSDT')
        valor_venda = doge_owned * doge_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"DOGE vendido por: {valor_venda:.2f} USDT")
        doge_owned = 0
        doge_purchase_price = 0.0

def vender_dot():
    global wallet, dot_owned, dot_purchase_price
    if dot_owned > 0:
        dot_usdt = get_price('DOTUSDT')
        valor_venda = dot_owned * dot_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"DOT vendido por: {valor_venda:.2f} USDT")
        dot_owned = 0
        dot_purchase_price = 0.0

def vender_ltc():
    global wallet, ltc_owned, ltc_purchase_price
    if ltc_owned > 0:
        ltc_usdt = get_price('LTCUSDT')
        valor_venda = ltc_owned * ltc_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"LTC vendido por: {valor_venda:.2f} USDT")
        ltc_owned = 0
        ltc_purchase_price = 0.0    

def vender_link():
    global wallet, link_owned, link_purchase_price
    if link_owned > 0:
        link_usdt = get_price('LINKUSDT')
        valor_venda = link_owned * link_usdt
        valor_venda = round(valor_venda, 2)
        wallet += valor_venda
        print(f"LINK vendido por: {valor_venda:.2f} USDT")
        link_owned = 0
        link_purchase_price = 0.0

def prot_exp():
    print("Protocolo de recuperação não implementado ainda.\n")
    return None

# Bots para cada cripto
def bot_1():
    global wallet, btc_owned, btc_purchase_price
    while True:
        pausar_evento.wait()
        time.sleep(1)

        btc_usdt = get_price('BTCUSDT')
        taxa_dolar = obter_taxa_dolar_para_real()
        btc_em_reais = btc_usdt * taxa_dolar

        print("--- BTC ---")
        print("Preço em USDT:", btc_usdt)
        print("Valor em Reais:", btc_em_reais)
        print("Valor atual da carteira:", wallet)
        print("BTC possuído:", btc_owned)
        print("BTC comprado:", btc_purchase_price)

        # Comprando...
        if btc_em_reais < 273000.00:
            if btc_owned == 0 and wallet > explosion:
                wallet -= take_value_btc
                btc_owned += take_value_btc / btc_usdt
                btc_purchase_price = btc_usdt
                print("Bitcoin comprado por:", take_value_btc)
                print("Nova carteira após compra:", wallet)
            else:
                print("Você já tem BTC comprado")
        else:
            print("Esperando para comprar...")

        # Lógica de venda
        if btc_owned > 0:
            target_price = btc_purchase_price * lucro_btc
            if btc_em_reais >= target_price * taxa_dolar:
                wallet += btc_owned * btc_usdt
                print("Bitcoin comprado por:", btc_purchase_price)
                print("Bitcoin vendido por:", btc_usdt)
                print("carteira atual:", wallet)
                btc_owned = 0
                btc_purchase_price = 0.0

        # Se o orçamento estourar, começa o protocolo:
        if wallet <= explosion:
            print("!!! Orçamento estourado !!!")
            print("Iniciando protocolo de recuperação...")
            prot_exp()
            while wallet < explosion:
                pass
        time.sleep(7)

def bot_2():
    global wallet, eth_owned, eth_purchase_price
    while True:
        pausar_evento.wait()
        time.sleep(2)

        eth_usdt = get_price('ETHUSDT')
        taxa_dolar = obter_taxa_dolar_para_real()
        eth_em_reais = eth_usdt * taxa_dolar

        print("--- ETH ---")
        print("Preço em USDT:", eth_usdt)
        print("Valor em Reais:", eth_em_reais)
        print("Valor atual da carteira:", wallet)
        print("ETH possuído:", eth_owned)
        print("ETH comprado:", eth_purchase_price)

        # Comprando...
        if eth_em_reais < 16000.00:  # Preço para compra
            if eth_owned == 0 and wallet > explosion:
                wallet -= take_value  # Valor a ser usado para compra
                eth_owned += take_value / eth_usdt
                eth_purchase_price = eth_usdt
                print("Ethereum comprado por:", take_value)
                print("Nova carteira após compra:", wallet)
            else:
                print("Você já tem ETH comprado")
        else:
            print("Esperando para comprar...")

        # Lógica de venda
        if eth_owned > 0:
            target_price = eth_purchase_price * lucro  # Lógica de lucro
            if eth_em_reais >= target_price * taxa_dolar:
                wallet += eth_owned * eth_usdt
                print("Ethereum vendido por:", eth_usdt)
                print("Nova carteira após venda:", wallet)
                eth_owned = 0
                eth_purchase_price = 0.0

        # Se o orçamento estourar, começa o protocolo:
        if wallet <= explosion:
            print("!!! Orçamento estourado !!!")
            print("Iniciando protocolo de recuperação...")
            prot_exp()
            while wallet < explosion:
                pass
        time.sleep(6)

def bot_3():
    global wallet, bnb_owned, bnb_purchase_price
    while True:
        pausar_evento.wait()
        time.sleep(3)

        bnb_usdt = get_price('BNBUSDT')
        taxa_dolar = obter_taxa_dolar_para_real()
        bnb_em_reais = bnb_usdt * taxa_dolar

        print("--- BNB ---")
        print("Preço em USDT:", bnb_usdt)
        print("Valor em Reais:", bnb_em_reais)
        print("Valor atual da carteira:", wallet)
        print("BNB possuído:", bnb_owned)
        print("BNB comprado:", bnb_purchase_price)

        # Comprando...
        if bnb_em_reais < 3400.00:
            if bnb_owned == 0.0:
                if wallet > explosion:
                    wallet -= take_value
                    bnb_owned += take_value / bnb_usdt
                    bnb_purchase_price = bnb_usdt
                    print("BNB comprado por:", take_value)
                    print("Nova carteira após compra:", wallet)
                else:
                    print("Orçamento insuficiente para compra.")
            else:
                print("Você já tem BNB comprada")
        else:
            print("Esperando para comprar...")

        # Lógica de venda
        if bnb_owned > 0:
            target_price = bnb_purchase_price * lucro
            if bnb_em_reais >= target_price * taxa_dolar:
                wallet += bnb_owned * bnb_usdt
                print("BNB vendido por:", bnb_usdt)
                print("Nova carteira após venda:", wallet)
                bnb_owned = 0
                bnb_purchase_price = 0.0

        # Se o orçamento estourar, começa o protocolo:
        if wallet <= explosion:
            print("!!! Orçamento estourado !!!")
            print("Iniciando protocolo de recuperação...")
            prot_exp()
            while wallet < explosion:
                pass
        time.sleep(5)

def bot_4():
    global wallet, ada_owned, ada_purchase_price
    while True:
        pausar_evento.wait()
        time.sleep(4)

        ada_usdt = get_price('ADAUSDT')
        taxa_dolar = obter_taxa_dolar_para_real()
        ada_em_reais = ada_usdt * taxa_dolar

        print("--- ADA ---")
        print("Preço em USDT:", ada_usdt)
        print("Valor em Reais:", ada_em_reais)
        print("Valor atual da carteira:", wallet)
        print("ADA possuído:", ada_owned)
        print("ADA comprado:", ada_purchase_price)

        # Comprando...
        if ada_em_reais < 2.40:
            if ada_owned == 0 and wallet > explosion:
                wallet -= take_value_ada
                ada_owned += take_value_ada / ada_usdt
                ada_purchase_price = ada_usdt
                print("ADA comprado por:", take_value_ada)
                print("Nova carteira após compra:", wallet)
            else:
                print("Você já tem ADA comprada")
        else:
            print("Esperando para comprar...")

        # Lógica de venda
        if ada_owned > 0:
            target_price = ada_purchase_price * lucro
            if ada_em_reais >= target_price * taxa_dolar:
                wallet += ada_owned * ada_usdt
                print("ADA vendido por:", ada_usdt)
                print("Nova carteira após venda:", wallet)
                ada_owned = 0
                ada_purchase_price = 0.0

        # Se o orçamento estourar, começa o protocolo:
        if wallet <= explosion:
            print("!!! Orçamento estourado !!!")
            print("Iniciando protocolo de recuperação...")
            prot_exp()
            while wallet < explosion:
                pass
        time.sleep(4)

def bot_5():
    global wallet, sol_owned, sol_purchase_price
    while True:
        pausar_evento.wait()
        time.sleep(5)

        sol_usdt = get_price('SOLUSDT')
        taxa_dolar = obter_taxa_dolar_para_real()
        sol_em_reais = sol_usdt * taxa_dolar

        print("--- SOL ---")
        print("Preço em USDT:", sol_usdt)
        print("Valor em Reais:", sol_em_reais)
        print("Valor atual da carteira:", wallet)
        print("SOL possuído:", sol_owned)
        print("SOL comprado:", sol_purchase_price)

        # Comprando...
        if sol_em_reais < 800.00:
            if sol_owned == 0 and wallet > explosion:
                wallet -= take_value_sol
                sol_owned += take_value_sol / sol_usdt
                sol_purchase_price = sol_usdt
                print("SOL comprado por:", take_value_sol)
                print("Nova carteira após compra:", wallet)
            else:
                print("Você já tem SOL comprado")
        else:
            print("Esperando para comprar...")

        # Lógica de venda
        if sol_owned > 0:
            target_price = sol_purchase_price * lucro
            if sol_em_reais >= target_price * taxa_dolar:
                wallet += sol_owned * sol_usdt
                print("SOL vendido por:", sol_usdt)
                print("Nova carteira após venda:", wallet)
                sol_owned = 0
                sol_purchase_price = 0.0

        # Se o orçamento estourar, começa o protocolo:
        if wallet <= explosion:
            print("!!! Orçamento estourado !!!")
            print("Iniciando protocolo de recuperação...")
            prot_exp()
            while wallet < explosion:
                pass
        time.sleep(3)

def bot_6():
    global wallet, xrp_owned, xrp_purchase_price
    while True:
        pausar_evento.wait()
        time.sleep(6)

        xrp_usdt = get_price('XRPUSDT')
        taxa_dolar = obter_taxa_dolar_para_real()
        xrp_em_reais = xrp_usdt * taxa_dolar

        print("--- XRP ---")
        print("Preço em USDT:", xrp_usdt)
        print("Valor em Reais:", xrp_em_reais)
        print("Valor atual da carteira:", wallet)
        print("XRP possuído:", xrp_owned)
        print("XRP comprado:", xrp_purchase_price)

        # Comprando...
        if xrp_em_reais < 3.50:
            if xrp_owned == 0 and wallet > explosion:
                wallet -= take_value_xrp
                xrp_owned += take_value_xrp / xrp_usdt
                xrp_purchase_price = xrp_usdt
                print("XRP comprado por:", take_value_xrp)
                print("Nova carteira após compra:", wallet)
            else:
                print("Você já tem XRP comprado")
        else:
            print("Esperando para comprar...")

        # Lógica de venda
        if xrp_owned > 0:
            target_price = xrp_purchase_price * lucro
            if xrp_em_reais >= target_price * taxa_dolar:
                wallet += xrp_owned * xrp_usdt
                print("XRP vendido por:", xrp_usdt)
                print("Nova carteira após venda:", wallet)
                xrp_owned = 0
                xrp_purchase_price = 0.0

        # Se o orçamento estourar, começa o protocolo:
        if wallet <= explosion:
            print("!!! Orçamento estourado !!!")
            print("Iniciando protocolo de recuperação...")
            prot_exp()
        time.sleep(2)

def bot_7():
    global wallet, doge_owned, doge_purchase_price
    while True:
        pausar_evento.wait()
        time.sleep(7)

        doge_usdt = get_price('DOGEUSDT')
        taxa_dolar = obter_taxa_dolar_para_real()
        doge_em_reais = doge_usdt * taxa_dolar

        print("--- DOGE ---")
        print("Preço em USDT:", doge_usdt)
        print("Valor em Reais:", doge_em_reais)
        print("Valor atual da carteira:", wallet)
        print("DOGE possuído:", doge_owned)
        print("DOGE comprado:", doge_purchase_price)

        # Comprando...
        if doge_em_reais < 0.50:
            if doge_owned == 0 and wallet > explosion:
                wallet -= take_value_doge
                doge_owned += take_value_doge / doge_usdt
                doge_purchase_price = doge_usdt
                print("DOGE comprado por:", take_value_doge)
                print("Nova carteira após compra:", wallet)
            else:
                print("Você já tem DOGE comprado")
        else:
            print("Esperando para comprar...")

        # Lógica de venda
        if doge_owned > 0:
            target_price = doge_purchase_price * lucro
            if doge_em_reais >= target_price * taxa_dolar:
                wallet += doge_owned * doge_usdt
                print("DOGE vendido por:", doge_usdt)
                print("Nova carteira após venda:", wallet)
                doge_owned = 0
                doge_purchase_price = 0.0

        # Se o orçamento estourar, começa o protocolo:
        if wallet <= explosion:
            print("!!! Orçamento estourado !!!")
            print("Iniciando protocolo de recuperação...")
            prot_exp()
        time.sleep(1)

# Adicionar novas funções para pausar e retomar
def pausar_threads():
    pausar_evento.clear()

def retomar_threads():
    pausar_evento.set()

# Iniciar os bots
thread1 = threading.Thread(target=bot_1)
thread2 = threading.Thread(target=bot_2)
thread3 = threading.Thread(target=bot_3)
thread4 = threading.Thread(target=bot_4)
thread5 = threading.Thread(target=bot_5)
thread6 = threading.Thread(target=bot_6)
thread7 = threading.Thread(target=bot_7)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()

def vender_item(item):
    if item == "btc":
        vender_btc()
        print("Bitcoin foi vendido.")
    elif item == "eth":
        vender_eth()
        print("Ethereum foi vendido.")
    elif item == "bnb":
        vender_bnb()
        print("BNB foi vendido.")
    elif item == "ada":
        vender_ada()
        print("ADA foi vendida.")
    elif item == "sol":
        vender_sol()
        print("SOL foi vendida.")
    elif item == "xrp":
        vender_xrp()
        print("XRP foi vendido.")
    elif item == "doge":
        vender_doge()
        print("DOGE foi vendido.")
    else:
        print(f"Item {item} não reconhecido.")

# Loop para controle de pausar e retomar

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    while True:
        comando = input()
        if comando == "stop":
            pausar_threads()
            print("Bots stopped.")
            print("Waiting...")
        elif comando == "run":
            retomar_threads()
            print("Bots running.")
        elif comando == "sell all":
            vender_btc()
            vender_eth()
            vender_bnb()
            vender_ada()
            vender_sol()
            vender_xrp()
            vender_doge()
            print("All cryptocurrencies sold.")
        elif comando.startswith("sell "):
            item = comando.split(" ")[1].lower()
            vender_item(item)
        elif comando == "wallet":
            print(f"Wallet balance: {wallet:.2f} USDT")
        elif comando.startswith("value my "):
            cripto = comando.split(" ")[2].lower()
            if cripto == "btc":
                print(f"You have {btc_owned:.6f} BTC.")
            elif cripto == "eth":
                print(f"You have {eth_owned:.6f} ETH.")
            elif cripto == "bnb":
                print(f"You have {bnb_owned:.6f} BNB.")
            elif cripto == "ada":
                print(f"You have {ada_owned:.6f} ADA.")
            elif cripto == "sol":
                print(f"You have {sol_owned:.6f} SOL.")
            elif cripto == "xrp":
                print(f"You have {xrp_owned:.6f} XRP.")
            elif cripto == "doge":
                print(f"You have {doge_owned:.6f} DOGE.")
            else:
                print("Unknown crypto.")
        elif comando.startswith("value buy "):
            cripto = comando.split(" ")[2].lower()
            if cripto == "btc":
                valor = get_price('BTCUSDT')
                print(f"1 BTC costs: {valor:.2f} USDT.")
            elif cripto == "eth":
                valor = get_price('ETHUSDT')
                print(f"1 ETH costs: {valor:.2f} USDT.")
            elif cripto == "bnb":
                valor = get_price('BNBUSDT')
                print(f"1 BNB costs: {valor:.2f} USDT.")
            elif cripto == "ada":
                valor = get_price('ADAUSDT')
                print(f"1 ADA costs: {valor:.2f} USDT.")
            elif cripto == "sol":
                valor = get_price('SOLUSDT')
                print(f"1 SOL costs: {valor:.2f} USDT.")
            elif cripto == "xrp":
                valor = get_price('XRPUSDT')
                print(f"1 XRP costs: {valor:.2f} USDT.")
            elif cripto == "doge":
                valor = get_price('DOGEUSDT')
                print(f"1 DOGE costs: {valor:.2f} USDT.")
            else:
                print("Unknown crypto.")
        elif comando == "balance":
            print(f"Current wallet balance: {wallet:.2f} USDT")
        elif comando == "portfolio":
            print("Current portfolio:")
            print(f"BTC: {btc_owned:.6f}, ETH: {eth_owned:.6f}, BNB: {bnb_owned:.6f}, ADA: {ada_owned:.6f}, SOL: {sol_owned:.6f}, XRP: {xrp_owned:.6f}, DOGE: {doge_owned:.6f}")
        elif comando == "help":
            print("Available commands:")
            print("- stop: Stop the bots.")
            print("- run: Start the bots.")
            print("- sell all: Sell all cryptocurrencies.")
            print("- sell [crypto]: Sell a specific cryptocurrency.")
            print("- wallet: Show wallet balance.")
            print("- value my [crypto]: Show how much of a specific crypto you own.")
            print("- value buy [crypto]: Show the current price of a specific crypto.")
            print("- balance: Show current wallet balance.")
            print("- portfolio: Show current holdings in the portfolio.")
        elif comando == "clear":
            clear_terminal()
            print("Terminal cleared.")
        elif comando.startswith("show "):
            cripto = comando.split(" ")[1].lower()
            # Aqui você deve adicionar a função que retorna as informações sobre a cripto
            if cripto == "btc":
                print(f"BTC: {btc_info}")  # Substitua `btc_info` pela sua função que retorna informações
            elif cripto == "eth":
                print(f"ETH: {eth_info}")
            elif cripto == "bnb":
                print(f"BNB: {bnb_info}")
            elif cripto == "ada":
                print(f"ADA: {ada_info}")
            elif cripto == "sol":
                print(f"SOL: {sol_info}")
            elif cripto == "xrp":
                print(f"XRP: {xrp_info}")
            elif cripto == "doge":
                print(f"DOGE: {doge_info}")
            else:
                print("Unknown crypto.")
except KeyboardInterrupt:
    print("Program terminated.")
