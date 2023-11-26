# from time import sleep
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole
from data.salvar_dados import salvar_dados

# Menu da funcionalidade 02 - Funcionalidade: Inserir novo gasto
def menu_inserir_gasto():
    limparConsole()
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
                salvar_dados(0, gastos, categoria)
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