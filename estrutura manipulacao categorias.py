def salvar_categorias(categorias):
    with open("categorias.txt", "w") as arquivo:
        for categoria in categorias:
            linha = f"{categoria['nome']},{categoria['limite']},{categoria['gasto']}\n"
            arquivo.write(linha)
def carregar_categorias():
    categorias = []
    try:
        with open("categorias.txt", "r") as arquivo:
            for linha in arquivo:
                nome, limite, gasto = linha.strip().split(',')
                categorias.append({
                    'nome': nome,
                    'limite': float(limite),
                    'gasto': float(gasto)
                })
        return categorias
    except FileNotFoundError:
        return []
