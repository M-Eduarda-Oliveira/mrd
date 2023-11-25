from time import sleep

# Inicio da estrutura de manipulação de arquivos
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

# Validação dos inputs
def input_valido(mensagem: object) -> object:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

# Menu Inicial
def menu_principal() -> object:
    while True:
        print("\nMenu Principal")
        print("1. Definir Categorias de Gastos e Limites")
        print("2. Inserir um Novo Gasto")
        print("3. Relatório de Gastos")
        print("4. Insights Financeiros")
        print("5. Sair")
        print("6. Exibir dados")

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
        elif escolha == 6:
            exibir_conteudo_arquivo()
            break
        else:
            print("\n\033[31mDigite uma opção válida, tente novamente.\033[m")
        sleep(1)

# Menu da funcionalidade 01 - Funcionalidade: Definir categorias de gasto
def menu_definir_categorias():
    while True:
        print("\nMenu de Categorias")
        print("1. Definir Orçamento Total Mensal")
        print("2. Editar Orçamento Total Mensal")
        print("3. Criar Categoria de Gastos")
        print("4. Editar Categoria de Gastos")
        print("5. Voltar ao Menu Principal")

        escolha = input_valido("Escolha uma opção: ")

        if escolha == 1:
            definir_orcamento()
        elif escolha == 2:
            editar_orcamento()
        elif escolha == 3:
            criar_categoria()
        elif escolha == 4:
            editar_categoria()
        elif escolha == 5:
            break
        else:
            print("Opção inválida, tente novamente.")

# Função: Definir orçamento mensal total
def definir_orcamento():
    try:
        orcamento = float(input("Digite o valor do orçamento total mensal: "))
        with open("orçamento.txt", "w") as arquivo:
            arquivo.write(str(orcamento))
        print("Orçamento definido com sucesso.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Função: Editar orçamento mensal total 
def editar_orcamento():
    try:
        with open("orçamento.txt", "r") as arquivo:
            orcamento_atual = arquivo.read()
        print(f"Orçamento atual: {orcamento_atual} ")

        novo_orcamento = float(input("Digite o novo valor do orçamento: "))
        with open("orçamento.txt", "w") as arquivo:
            arquivo.write(str(novo_orcamento))
        print("Orçamento atualizado com sucesso.")
    except FileNotFoundError:
        print("Orçamento não definido. Defina um orçamento primeiro.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Função: Criar nova categoria de gasto
def criar_categoria():
    nova_categoria = input("Digite o nome da nova categoria de gasto: ")
    limite = float(input("Defina um limite de gastos para esta categoria: "))
    with open("categorias.txt", "a") as arquivo:
        arquivo.write(f"{nova_categoria}: {limite}\n")
    print("Categoria criada com sucesso.")


# Função: Ediatar categoria de gastos
def editar_categoria():
    categoria_a_editar = input("Digite o nome da categoria que deseja editar: ")
    novo_nome = input("Digite o novo nome da categoria: ")
    novo_limite = float(input("Defina o novo limite de gastos para esta categoria: "))
    print("Categoria editada com sucesso.")

# Menu da funcionalidade 02 - Funcionalidade: Inserir novo gasto
def menu_inserir_gasto():
    while True:
        categorias = ler_categorias()
        if not categorias:
            print("Nenhuma categoria encontrada. Adicione categorias primeiro.")
            break

        print("\nInserir Novo Gasto")
        for key, value in categorias.items():
            print(f"{key}. {value}")
        print(f"{len(categorias) + 1}. Voltar ao Menu Principal")

        escolha = input_valido("Escolha uma opção: ")

        if escolha in categorias:
            try:
                gastos = float(input("Digite o valor do gasto: "))
                if gastos < 0:
                    raise ValueError("O valor do gasto não pode ser negativo.")  # Para impedir o uso de valores negativos.

                categoria = categorias[escolha]
                salvar_dados(gastos, categoria)
            except ValueError as e:
                print(f"Erro: {e}. Por favor, insira um valor válido.")
        elif escolha == len(categorias) + 1:
            break
        else:
            print("Opção inválida, tente novamente.")

# Função: Mostrar categorias de gastos definidas pelo usuário
def ler_categorias() -> object:
    categorias = {}
    try:
        with open("categorias.txt", "rt") as arquivo:
            for linha in arquivo:
                nome, _ = linha.strip().split(':')
                categorias[len(categorias) + 1] = nome
    except FileNotFoundError:
        print("Arquivo de categorias não encontrado.")
    return categorias

# Menu da funcionalidade 03 - Funcionalidade: Relatório de gastos
def menu_relatorio_gastos():
    while True:
        print("\nRelatório de Gastos")
        print("1. Relatório de Gasto Geral")
        print("2. Relatório de Gasto por Categoria")
        print("3. Voltar ao Menu Principal")

        escolha = input_valido("Escolha uma opção: ")

        if escolha == 1:
            relatorio_geral()
        elif escolha == 2:
            relatorio_por_categoria()
        elif escolha == 3:
            break
        else:
            print("Opção inválida, tente novamente.")

# Função: Exibir relatório de gastos a partir da categoria selecionada
def relatorio_por_categoria():
    categoria_especifica = input("Digite a categoria para a qual deseja o relatório: ")
    try:
        with open("dados_financeiros.txt", "r") as arquivo:
            for linha in arquivo:
                if categoria_especifica in linha:
                    print(linha.strip())
    except FileNotFoundError:
        print("Nenhum dado de gasto encontrado.")

# Função: Exibir relatório de gastos de todas as categorias
def relatorio_geral():
    try:
        with open("dados_financeiros.txt", "r") as arquivo:
            for linha in arquivo:
                print(linha.strip())
    except FileNotFoundError:
        print("Nenhum dado de gasto encontrado.")

# Menu da funcionalidade 04 - Funcionalidade: Insights Financeiros
def menu_insights_financeiros():
    saldo_total = ler_dados()
    orçamento = ler_orcamento()

    if saldo_total > orçamento:
        print("Parece que você gastou mais que o seu orçamento. Já pensou em economizar as saídas no domingo?")
    else:
        print(
            "Ótimo! Você está dentro do orçamento. Já pensou em investir seu rico dinheirinho para render ainda mais?")

# Função: Ler e mostrar relatório de orçamento do usuário
def ler_orcamento():
    try:
        with open("orçamento.txt", "r") as arquivo:
            orçamento = float(arquivo.read())
            return orçamento
    except FileNotFoundError:
        print("Arquivo de orçamento não encontrado. Defina um orçamento primeiro.")
        return 0

# Função para exibir todos os dados
def exibir_conteudo_arquivo():
    try:
        with open("dados_financeiros.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
menu_principal()
