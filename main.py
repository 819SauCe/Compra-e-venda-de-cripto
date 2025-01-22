import time

while True:
    try:
        import pendulum
        import numpy as np
        import psycopg2
        from psycopg2.pool import SimpleConnectionPool
        from sklearn.linear_model import LinearRegression
        from api import *

        # Conexão com o banco
        pool = SimpleConnectionPool(1, 10, user="postgres", password="979838870", host="localhost", database="Cripto")
        conn = pool.getconn()
        cursor = conn.cursor()

        # Selecionando os dados das criptomoedas
        cursor.execute("SELECT * FROM cripto WHERE cripto = %s", ('BTCUSDT',))
        btc_dados = cursor.fetchall()
        cursor.execute("SELECT * FROM cripto WHERE cripto = %s", ('ETHUSDT',))
        eth_dados = cursor.fetchall()
        cursor.execute("SELECT * FROM cripto WHERE cripto = %s", ('BNBUSDT',))
        bnb_dados = cursor.fetchall()
        cursor.execute("SELECT * FROM cripto WHERE cripto = %s", ('ADAUSDT',))
        ada_dados = cursor.fetchall()
        cursor.execute("SELECT * FROM cripto WHERE cripto = %s", ('SOLUSDT',))
        sol_dados = cursor.fetchall()
        cursor.execute("SELECT * FROM cripto WHERE cripto = %s", ('XRPUSDT',))
        xrp_dados = cursor.fetchall()
        cursor.execute("SELECT * FROM cripto WHERE cripto = %s", ('DOGEUSDT',))
        doge_dados = cursor.fetchall()

        # Extraindo os preços e datas dos dados
        btc_precos = [linha[2] for linha in btc_dados]
        btc_datas = [linha[1] for linha in btc_dados]
        eth_precos = [linha[2] for linha in eth_dados]
        eth_datas = [linha[1] for linha in eth_dados]
        bnb_precos = [linha[2] for linha in bnb_dados]
        bnb_datas = [linha[1] for linha in bnb_dados]
        ada_precos = [linha[2] for linha in ada_dados]
        ada_datas = [linha[1] for linha in ada_dados]
        sol_precos = [linha[2] for linha in sol_dados]
        sol_datas = [linha[1] for linha in sol_dados]
        xrp_precos = [linha[2] for linha in xrp_dados]
        xrp_datas = [linha[1] for linha in xrp_dados]
        doge_precos = [linha[2] for linha in doge_dados]
        doge_datas = [linha[1] for linha in doge_dados]

        # Criando arrays para cada criptomoeda
        btc_precos_array = np.array(btc_precos).reshape(-1, 1)
        X_btc = np.arange(len(btc_precos)).reshape(-1, 1)
        eth_precos_array = np.array(eth_precos).reshape(-1, 1)
        X_eth = np.arange(len(eth_precos)).reshape(-1, 1)
        bnb_precos_array = np.array(bnb_precos).reshape(-1, 1)
        X_bnb = np.arange(len(bnb_precos)).reshape(-1, 1)
        ada_precos_array = np.array(ada_precos).reshape(-1, 1)
        X_ada = np.arange(len(ada_precos)).reshape(-1, 1)
        sol_precos_array = np.array(sol_precos).reshape(-1, 1)
        X_sol = np.arange(len(sol_precos)).reshape(-1, 1)
        xrp_precos_array = np.array(xrp_precos).reshape(-1, 1)
        X_xrp = np.arange(len(xrp_precos)).reshape(-1, 1)
        doge_precos_array = np.array(doge_precos).reshape(-1, 1)
        X_doge = np.arange(len(doge_precos)).reshape(-1, 1)

        # IA para cada criptomoeda
        model_btc = LinearRegression()
        model_btc.fit(X_btc, btc_precos_array)
        model_eth = LinearRegression()
        model_eth.fit(X_eth, eth_precos_array)
        model_bnb = LinearRegression()
        model_bnb.fit(X_bnb, bnb_precos_array)
        model_ada = LinearRegression()
        model_ada.fit(X_ada, ada_precos_array)
        model_sol = LinearRegression()
        model_sol.fit(X_sol, sol_precos_array)
        model_xrp = LinearRegression()
        model_xrp.fit(X_xrp, xrp_precos_array)
        model_doge = LinearRegression()
        model_doge.fit(X_doge, doge_precos_array)

        # Previsões para cada criptomoeda
        proximo_preco_btc = round(model_btc.predict([[len(btc_precos)]])[0][0], 2)
        proximo_preco_eth = round(model_eth.predict([[len(eth_precos)]])[0][0], 2)
        proximo_preco_bnb = round(model_bnb.predict([[len(bnb_precos)]])[0][0], 2)
        proximo_preco_ada = round(model_ada.predict([[len(ada_precos)]])[0][0], 2)
        proximo_preco_sol = round(model_sol.predict([[len(sol_precos)]])[0][0], 2)
        proximo_preco_xrp = round(model_xrp.predict([[len(xrp_precos)]])[0][0], 2)
        proximo_preco_doge = round(model_doge.predict([[len(doge_precos)]])[0][0], 2)

        # Preço cripto atual
        curret_btc = get_price('BTCUSDT')
        curret_eth = get_price('ETHUSDT')
        curret_bnb = get_price('BNBUSDT')
        curret_ada = get_price('ADAUSDT')
        curret_sol = get_price('SOLUSDT')
        curret_xrp = get_price('XRPUSDT')
        curret_doge = get_price('DOGEUSDT')

        # Print dos resultados
        print(f"{'Criptomoeda':<15} | {'Próximo Preço':<15} | {'Preço Atual':<15}")
        print("-" * 50)
        print(f"{'BTC':<15} | {proximo_preco_btc:<15} | {curret_btc:<15}")
        print(f"{'ETH':<15} | {proximo_preco_eth:<15} | {curret_eth:<15}")
        print(f"{'BNB':<15} | {proximo_preco_bnb:<15} | {curret_bnb:<15}")
        print(f"{'ADA':<15} | {proximo_preco_ada:<15} | {curret_ada:<15}")
        print(f"{'SOL':<15} | {proximo_preco_sol:<15} | {curret_sol:<15}")
        print(f"{'XRP':<15} | {proximo_preco_xrp:<15} | {curret_xrp:<15}")
        print(f"{'DOGE':<15} | {proximo_preco_doge:<15} | {curret_doge:<15}")
        print("-" * 50)

        wallet = 1.68
        compra_controlada = wallet / 10
        saldo_inicial = wallet

        btc_balance = 0.0
        eth_balance = 0.0
        bnb_balance = 0.0
        ada_balance = 0.0
        sol_balance = 0.0
        xrp_balance = 0.0
        doge_balance = 0.0
        preco_compra = 0.0

        def buy_btc():
            global wallet, btc_balance, preco_compra
            fração_btc = compra_controlada / curret_btc
            wallet -= compra_controlada
            btc_balance += fração_btc
            preco_compra = curret_btc
            print(f"Você comprou {fração_btc:.8f} BTC")
            print(f"Saldo atual: {wallet:.2f}, BTC: {btc_balance:.8f}")

        def sell_btc():
            global wallet, btc_balance
            fração_btc = btc_balance
            venda_total = fração_btc * curret_btc
            wallet += venda_total
            btc_balance = 0.0
            print(f"Você vendeu {fração_btc:.8f} BTC")
            print(f"Saldo atual: {wallet:.2f}, BTC: {btc_balance:.8f}")

        def buy_eth():
            global wallet, eth_balance, preco_compra
            fração_eth = compra_controlada / curret_eth
            wallet -= compra_controlada
            eth_balance += fração_eth
            preco_compra = curret_eth
            print(f"Você comprou {fração_eth:.8f} ETH")
            print(f"Saldo atual: {wallet:.2f}, ETH: {eth_balance:.8f}")

        def sell_eth():
            global wallet, eth_balance
            fração_eth = eth_balance
            venda_total = fração_eth * curret_eth
            wallet += venda_total
            eth_balance = 0.0
            print(f"Você vendeu {fração_eth:.8f} ETH")
            print(f"Saldo atual: {wallet:.2f}, ETH: {eth_balance:.8f}")

        def buy_bnb():
            global wallet, bnb_balance, preco_compra
            fração_bnb = compra_controlada / curret_bnb
            wallet -= compra_controlada
            bnb_balance += fração_bnb
            preco_compra = curret_bnb
            print(f"Você comprou {fração_bnb:.8f} BNB")
            print(f"Saldo atual: {wallet:.2f}, BNB: {bnb_balance:.8f}")

        def sell_bnb():
            global wallet, bnb_balance
            fração_bnb = bnb_balance
            venda_total = fração_bnb * curret_bnb
            wallet += venda_total
            bnb_balance = 0.0
            print(f"Você vendeu {fração_bnb:.8f} BNB")
            print(f"Saldo atual: {wallet:.2f}, BNB: {bnb_balance:.8f}")

        def buy_ada():
            global wallet, ada_balance, preco_compra
            fração_ada = compra_controlada / curret_ada
            wallet -= compra_controlada
            ada_balance += fração_ada
            preco_compra = curret_ada
            print(f"Você comprou {fração_ada:.8f} ADA")
            print(f"Saldo atual: {wallet:.2f}, ADA: {ada_balance:.8f}")

        def sell_ada():
            global wallet, ada_balance
            fração_ada = ada_balance
            venda_total = fração_ada * curret_ada
            wallet += venda_total
            ada_balance = 0.0
            print(f"Você vendeu {fração_ada:.8f} ADA")
            print(f"Saldo atual: {wallet:.2f}, ADA: {ada_balance:.8f}")

        def buy_sol():
            global wallet, sol_balance, preco_compra
            fração_sol = compra_controlada / curret_sol
            wallet -= compra_controlada
            sol_balance += fração_sol
            preco_compra = curret_sol
            print(f"Você comprou {fração_sol:.8f} SOL")
            print(f"Saldo atual: {wallet:.2f}, SOL: {sol_balance:.8f}")

        def sell_sol():
            global wallet, sol_balance
            fração_sol = sol_balance
            venda_total = fração_sol * curret_sol
            wallet += venda_total
            sol_balance = 0.0
            print(f"Você vendeu {fração_sol:.8f} SOL")
            print(f"Saldo atual: {wallet:.2f}, SOL: {sol_balance:.8f}")

        def buy_xrp():
            global wallet, xrp_balance, preco_compra
            fração_xrp = compra_controlada / curret_xrp
            wallet -= compra_controlada
            xrp_balance += fração_xrp
            preco_compra = curret_xrp
            print(f"Você comprou {fração_xrp:.8f} XRP")
            print(f"Saldo atual: {wallet:.2f}, XRP: {xrp_balance:.8f}")

        def sell_xrp():
            global wallet, xrp_balance
            fração_xrp = xrp_balance
            venda_total = fração_xrp * curret_xrp
            wallet += venda_total
            xrp_balance = 0.0
            print(f"Você vendeu {fração_xrp:.8f} XRP")
            print(f"Saldo atual: {wallet:.2f}, XRP: {xrp_balance:.8f}")

        def buy_doge():
            global wallet, doge_balance, preco_compra
            fração_doge = compra_controlada / curret_doge
            wallet -= compra_controlada
            doge_balance += fração_doge
            preco_compra = curret_doge
            print(f"Você comprou {fração_doge:.8f} DOGE")
            print(f"Saldo atual: {wallet:.2f}, DOGE: {doge_balance:.8f}")

        def sell_doge():
            global wallet, doge_balance
            fração_doge = doge_balance
            venda_total = fração_doge * curret_doge
            wallet += venda_total
            doge_balance = 0.0
            print(f"Você vendeu {fração_doge:.8f} DOGE")
            print(f"Saldo atual: {wallet:.2f}, DOGE: {doge_balance:.8f}")

        if btc_balance > 0 and current_btc >= preco_compra * 1.1:
            sell_btc()

        if btc_balance == 0 and wallet >= compra_controlada:
            buy_btc()

        if eth_balance > 0 and curret_eth >= preco_compra * 1.1:
            sell_eth()

        if eth_balance == 0 and wallet >= compra_controlada:
            buy_eth()

        if bnb_balance > 0 and curret_bnb >= preco_compra * 1.1:
            sell_bnb()

        if bnb_balance == 0 and wallet >= compra_controlada:
            buy_bnb()

        if ada_balance > 0 and curret_ada >= preco_compra * 1.1:
            sell_ada()

        if ada_balance == 0 and wallet >= compra_controlada:
            buy_ada()

        if sol_balance > 0 and curret_sol >= preco_compra * 1.1:
            sell_sol()

        if sol_balance == 0 and wallet >= compra_controlada:
            buy_sol()

        if xrp_balance > 0 and curret_xrp >= preco_compra * 1.1:
            sell_xrp()

        if xrp_balance == 0 and wallet >= compra_controlada:
            buy_xrp()

        if doge_balance > 0 and curret_doge >= preco_compra * 1.1:
            sell_doge()

        if doge_balance == 0 and wallet >= compra_controlada:
            buy_doge()

        def patrimonio_total():
            return (wallet + 
                    btc_balance * curret_btc +
                    eth_balance * curret_eth +
                    bnb_balance * curret_bnb +
                    ada_balance * curret_ada +
                    sol_balance * curret_sol +
                    xrp_balance * curret_xrp +
                    doge_balance * curret_doge)
        print(f"Patrimônio total: {patrimonio_total():.2f}")
        if patrimonio_total() > saldo_inicial:
            print("Você está lucrando!")
        else:
            print("Ainda não obteve lucro.")


        pool.closeall()
    except Exception as e:
        print(f"Erro: {e}")
    time.sleep(60)
