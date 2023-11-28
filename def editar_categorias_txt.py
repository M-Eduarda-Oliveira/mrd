def editar_categoria():
    global categorias
    nome_categoria = input("Digite o nome da categoria que deseja editar: ")

    if nome_categoria not in categorias:
        print("Categoria não encontrada.")
        return

    novo_limite = float(input(f"Defina um novo limite de gastos para a categoria '{nome_categoria}': "))
    categorias[nome_categoria] = novo_limite

    with open("categorias.txt", "w") as arquivo:
        for categoria, lim in categorias.items():
            arquivo.write(f"{categoria}: {lim}\n")

    print("Categoria editada com sucesso.")
