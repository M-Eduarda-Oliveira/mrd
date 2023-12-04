from asyncio import sleep
from data.exibir_dados import exibir_conteudo_arquivo
from services.categorias_gastos import menu_definir_categorias
from services.inserir_gasto import menu_inserir_gasto
from services.insights import menu_insights_financeiros
from services.relatorio import menu_relatorio_gastos
from utils.limpar_console import limparConsole
from utils.validacao_input import input_valido
import sys

def menu_principal():
    limparConsole(1)
    print("\nMenu Principal \n 1. Definir Categorias de Despesas e Limites \n 2. Inserir um Novo Gasto \n 3. Relatório de Gastos \n 4. Insights Financeiros \n 5. Sair")
    escolha = input_valido("Escolha uma opção: ")

    if escolha == 1:
        limparConsole(1)
        menu_definir_categorias()
    elif escolha == 2:
        limparConsole(1)
        menu_inserir_gasto()
    elif escolha == 3:
        limparConsole(1)
        menu_relatorio_gastos()
    elif escolha == 4:
        limparConsole(1)
        menu_insights_financeiros()
    elif escolha == 5:
        from data.salvar_dados import salvar_dicionario
        from data.registros_categorias import registrosGerais
        salvar_dicionario(registrosGerais)
        sys.exit()
    else:
        print("\n\033[31mDigite uma opção válida, tente novamente.\033[m")
        limparConsole(2)