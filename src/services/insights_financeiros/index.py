from time import sleep
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole
from main import ler_dados

# Menu da funcionalidade 04 - Funcionalidade: Insights Financeiros
def menu_insights_financeiros():
    limparConsole()
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