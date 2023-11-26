import os
from time import sleep
from data.exibir_dados import exibir_conteudo_arquivo
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole
from services.categorias_e_limites.index import menu_definir_categorias
from services.novo_gasto.index import menu_inserir_gasto
from services.relatorio_gastos.index import menu_relatorio_gastos
from services.insights_financeiros.index import menu_insights_financeiros

inicio = input("Podemos Iniciar o Programa?\nDigite 'S' para Sim, ou 'N' para Não: ").upper()
# limparConsole()

# Menu Inicial
while(inicio == "S"):
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
        break
    elif escolha == 6:
        limparConsole()
        exibir_conteudo_arquivo()
        break
    else:
        print("\n\033[31mDigite uma opção válida, tente novamente.\033[m")
        limparConsole()
        sleep(1)
else:
    if(inicio == "N"):
        print('============================================================')
        print("Programa encerrado.")
        print('============================================================')
    elif(inicio != "N" or "S"):
        print('============================================================')
        print("Digite uma opção válida.")
        print('============================================================')
