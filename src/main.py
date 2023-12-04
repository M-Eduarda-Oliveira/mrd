from time import sleep
from data.exibir_dados import exibir_conteudo_arquivo
from menu_principal import menu_principal
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole
from services.categorias_gastos import menu_definir_categorias
from services.inserir_gasto import menu_inserir_gasto
from services.relatorio import menu_relatorio_gastos
from services.insights import menu_insights_financeiros

def menu_main():
    inicio = input("Podemos Iniciar o Programa?\nDigite 'S' para Sim, ou 'N' para Não: ").upper()
    limparConsole(1)
    # Menu Inicial
    while(inicio == "S"):
        from data.carregar_dados import carregar_dicionario
        from data.registros_categorias import registrosGerais
        carregar_dicionario(registrosGerais)
        opcao = menu_principal()
        if (opcao == 5): break

    if(inicio == "N"):
        print('============================================================')
        print("Programa encerrado.")
        print('============================================================')
    elif(inicio != "N" or "S"):
        print('============================================================')
        print("Digite uma opção válida.")
        print('============================================================')
    
menu_main()