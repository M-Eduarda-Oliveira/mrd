def ler_dados():
    saldo_total = 0
    try:
        with open("dados_financeiros.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.split(',')
                ganhos = float(partes[0].split(':')[1].strip())
                gastos = float(partes[1].split(':')[1].strip())
                saldo_total += (ganhos - gastos)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Será criado um novo arquivo.")
    return saldo_total
