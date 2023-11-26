def salvar_dados(gastos, categoria):
    with open("dados_financeiros.txt", "a") as arquivo:
        arquivo.write(f"Gastos: {gastos}, Categoria: {categoria}\n")