from time import sleep
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole

# Menu da funcionalidade 03 - Funcionalidade: Relatório de gastos
def menu_relatorio_gastos():
    while True:
        print("\nRelatório de Gastos \n 1. Relatório de Gasto Geral \n 2. Relatório de Gasto por Categoria \n 3. Voltar ao Menu Principal")
        escolha = input_valido("Escolha uma opção: ")

        if escolha == 1:
            limparConsole()
            relatorio_geral()
        elif escolha == 2:
            limparConsole()
            relatorio_por_categoria()
        elif escolha == 3:
            break
        else:
            print("Opção inválida, tente novamente.")
            limparConsole()

# Função: Exibir relatório de gastos de todas as categorias
def relatorio_geral():
    try:
        with open("dados_financeiros.txt", "r") as arquivo:
            for linha in arquivo:
                print(linha.strip())
                with open("categorias.txt", "r") as arquivo:
                        for linha in arquivo:
                            print("O limite é " + linha.strip())
    except FileNotFoundError:
        print("Nenhum dado de gasto encontrado.")

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