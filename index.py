def salvar_dados(ganhos, gastos, categoria):
    with open("dados_financeiros.txt", "a") as arquivo:
        arquivo.write(f"Ganhos: {ganhos}, Gastos: {gastos}, Categoria: {categoria}\n")
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
def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Definir Categorias de Gastos e Limites")
        print("2. Inserir um Novo Gasto")
        print("3. Relatório de Gastos")
        print("4. Insights Financeiros")
        print("5. Sair")
        escolha = input_valido("Escolha uma opção: ")
        if escolha == 1:
            menu_definir_categorias()
        elif escolha == 2:
            menu_inserir_gasto()
        elif escolha == 3:
            menu_relatorio_gastos()
        elif escolha == 4:
            menu_insights_financeiros()
        elif escolha == 5:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, tente novamente.")
def menu_definir_categorias():
    while True:
        print("\nMenu de Categorias")
        print("1. Definir Orçamento Total Mensal")
        print("2. Criar Categorias de Gastos e seus Limites")
        print("3. Voltar ao Menu Principal")
        escolha = input_valido("Escolha uma opção: ")
        if escolha == 1:
            # Implementar lógica para definir orçamento
            pass
        elif escolha == 2:
            # Implementar lógica para criar categorias e limites
            pass
        elif escolha == 3:
            break
        else:
            print("Opção inválida, tente novamente.")
def menu_inserir_gasto():
    while True:
        print("\nInserir Novo Gasto")
        print("1. Categoria 1")
        print("2. Categoria 2")
        print("3. Categoria 3")
        print("4. Voltar ao Menu Principal")
        escolha = input_valido("Escolha uma opção: ")
        if escolha in [1, 2, 3]:
            try:
                gastos = float(input("Digite o valor do gasto: "))
                if gastos < 0:
                    raise ValueError("O valor do gasto não pode ser negativo.")
                categorias = {1: "Categoria 1", 2: "Categoria 2", 3: "Categoria 3"}
                categoria = categorias[escolha]
                ganhos = 1000  # Valor fixo para exemplo. Em um aplicativo real, seria dinâmico.
                salvar_dados(ganhos, gastos, categoria)
            except ValueError as e:
                print(f"Erro: {e}. Por favor, insira um valor válido.")
        elif escolha == 4:
            break
        else:
            print("Opção inválida, tente novamente.")
def menu_relatorio_gastos():
    while True:
        print("\nRelatório de Gastos")
        print("1. Relatório de Gasto Geral")
        print("2. Relatório de Gasto por Categoria")
        print("3. Voltar ao Menu Principal")
        escolha = input_valido("Escolha uma opção: ")
        if escolha == 1:
            # Implementar lógica para relatório de gasto geral
            pass
        elif escolha == 2:
            # Implementar lógica para relatório de gasto por categoria
            pass
        elif escolha == 3:
            break
        else:
            print("Opção inválida, tente novamente.")
def input_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")
def menu_insights_financeiros():
    # Implementar a lógica dos insights financeiros
    pass
# Iniciando o programa
menu_principal()
