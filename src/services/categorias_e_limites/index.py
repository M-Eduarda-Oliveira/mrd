from time import sleep
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole
# Menu da funcionalidade 01 - Funcionalidade: Definir categorias de gasto
def menu_definir_categorias():
    while True:
        print('''Menu de Categorias\n 1. Definir Orçamento Total Mensal\n 2. Editar Orçamento Total Mensal\n 3. Criar Categoria de Gastos\n 4. Editar Categoria de Gastos\n 5. Voltar ao Menu Principal''')
        escolha = input_valido("Escolha uma opção: ")

        if escolha == 1:
            limparConsole()
            definir_orcamento()
        elif escolha == 2:
            limparConsole()
            editar_orcamento()
        elif escolha == 3:
            limparConsole()
            criar_categoria()
        elif escolha == 4:
            limparConsole()
            editar_categoria()
        elif escolha == 5:
            break
        else:
            print("Opção inválida, tente novamente.")
            limparConsole()

# Função: Definir orçamento mensal total
def definir_orcamento():
    try:
        orcamento = float(input("Digite o valor do orçamento total mensal: "))
        with open("orçamento.txt", "w") as arquivo:
            arquivo.write(str(orcamento))
        print("Orçamento definido com sucesso.")
        sleep(1)
        limparConsole()
    except ValueError:
        print("Por favor, insira um número válido.")
        sleep(1)
        limparConsole()


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
        sleep(1)
        limparConsole()

    except FileNotFoundError:
        print("Orçamento não definido. Defina um orçamento primeiro.")
        sleep(1)
        limparConsole()
    except ValueError:
        print("Por favor, insira um número válido.")
        sleep(1)
        limparConsole()

# Função: Criar nova categoria de gasto
def criar_categoria():
    nova_categoria = input("Digite o nome da nova categoria de gasto: ")
    limite = float(input("Defina um limite de gastos para esta categoria: "))
    with open("categorias.txt", "a") as arquivo:
        arquivo.write(f"{nova_categoria}: {limite}\n")
    print("Categoria criada com sucesso.")
    sleep(1)
    limparConsole()


# Função: Editar categoria de gastos
def editar_categoria():
    categoria_a_editar = input("Digite o nome da categoria que deseja editar: ")
    novo_nome = input("Digite o novo nome da categoria: ")
    novo_limite = float(input("Defina o novo limite de gastos para esta categoria: "))
    print("Categoria editada com sucesso.")
