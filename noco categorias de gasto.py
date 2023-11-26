
categorias = {}
gastos_por_categoria = {}  # Dicionários

def criar_categoria():
    nome = input("Digite o nome da nova categoria de gasto: ")
    limite = float(input("Defina um limite de gastos para esta categoria: "))
    categorias[nome] = limite
    print("Categoria criada com sucesso.")

def editar_categoria():
    nome = input("Digite o nome da categoria que deseja editar: ")
    if nome in categorias:
        novo_nome = input("Digite o novo nome da categoria: ")
        novo_limite = float(input("Defina o novo limite de gastos para esta categoria: "))
        categorias.pop(nome)
        categorias[novo_nome] = novo_limite
        print("Categoria editada com sucesso.")
    else:
        print("Categoria não encontrada.")

def adicionar_gasto():
    print("\nCategorias Disponíveis:")
    for nome in categorias:
        print(nome)
    categoria = input("Escolha uma categoria: ")
    if categoria in categorias:
        valor = float(input("Digite o valor do gasto: "))
        if categoria not in gastos_por_categoria:
            gastos_por_categoria[categoria] = []
        gastos_por_categoria[categoria].append(valor)
        print("Gasto adicionado.")
    else:
        print("Categoria não encontrada.")

def relatorio_gastos():
    print("\nRelatório de Gastos:")
    for categoria, gastos in gastos_por_categoria.items():
        total_gasto = sum(gastos)
        print(f"Categoria: {categoria}, Gastos: {total_gasto}")


menu_principal()
