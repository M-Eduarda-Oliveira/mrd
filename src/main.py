from time import sleep
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole
from services.categorias_e_limites.index import menu_definir_categorias
from services.novo_gasto.index import menu_inserir_gasto
from services.relatorio_gastos.index import menu_relatorio_gastos
from services.insights_financeiros.index import menu_insights_financeiros

# Inicio da estrutura de manipulação de arquivos
def salvar_dados(gastos, categoria):
    with open("dados_financeiros.txt", "a") as arquivo:
        arquivo.write(f"Gastos: {gastos}, Categoria: {categoria}\n")


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

# Menu Inicial
def menu_principal() -> object:
    while True:
        print("\nMenu Principal \n 1. Definir Categorias de Gastos e Limites \n 2. Inserir um Novo Gasto \n 3. Relatório de Gastos \n 4. Insights Financeiros \n 5. Sair \n 6. Exibir dados")
        escolha = input_valido("Escolha uma opção: ")

        if escolha == 1:
            limparConsole()
            menu_definir_categorias()
        elif escolha == 2:
            limparConsole()
            menu_inserir_gasto()
        elif escolha == 3:
            limparConsole()
            menu_relatorio_gastos()
        elif escolha == 4:
            limparConsole()
            menu_insights_financeiros()
        elif escolha == 5:
            limparConsole()
            print("Saindo do programa.")
        elif escolha == 6:
            limparConsole()
            exibir_conteudo_arquivo()
            break
        else:
            print("\n\033[31mDigite uma opção válida, tente novamente.\033[m")
            limparConsole()
        sleep(1)

# Função para exibir todos os dados
def exibir_conteudo_arquivo():
    try:
        with open("dados_financeiros.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")

menu_principal()
