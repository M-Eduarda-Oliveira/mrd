categorias = {
    "Geral": {"limite": None, "gastos": 0},
    "Saúde": {"limite": None, "gastos": 0},
    "Educação": {"limite": None, "gastos": 0}
}

def adicionar_categoria():
    global categorias
    nome = input("Digite o nome da nova categoria: ")
    if nome in categorias:
        print("Categoria já existe.")
        return
    categorias[nome] = {"limite": None, "gastos": 0}
    print("Categoria adicionada com sucesso.")
