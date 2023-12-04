from time import sleep
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole

# Menu da funcionalidade 03 - Funcionalidade: Relatório de gastos
def menu_relatorio_gastos():
    print("\nRelatório de Gastos \n 1. Relatório de Gasto Geral \n 2. Relatório de Gasto por Categoria \n 3. Voltar ao Menu Principal")
    escolha = input_valido("Escolha uma opção: ")

    if escolha == 1:
        limparConsole(0)
        relatorio_geral()
    elif escolha == 2:
        limparConsole(0)
        relatorio_por_categoria()
    elif escolha == 3:
        limparConsole(0)
        from menu_principal import menu_principal
        menu_principal()
    else:
        print("Opção inválida, tente novamente.")
        limparConsole(1)

# Função: Exibir relatório de gastos de todas as categorias
def relatorio_geral():
    from data.registros_categorias import registrosGerais
    orcamentoMensal = registrosGerais['orcamentoMensal']
    gastosTotais = 0
    for categoria in registrosGerais['categorias']:
        gastosTotais += float(categoria['gasto'])
    resto = (orcamentoMensal - gastosTotais)
    print(f"Até o momento você gastou o total de {gastosTotais} reais. \nO limite que você definiu para esse mês foi de {orcamentoMensal} reais. \n Restou {resto} reais do seu total mensal.")
    limparConsole(4)
    menu_relatorio_gastos()

# Função: Exibir relatório de gastos a partir da categoria selecionada
def relatorio_por_categoria():
    from data.registros_categorias import registrosGerais
    print('============================================================')
    for (categoria) in registrosGerais['categorias']:
        index = registrosGerais['categorias'].index(categoria)
        print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais. Você já gastou {categoria['gasto']} reais.")
    print('============================================================')
    limparConsole(4)
    menu_relatorio_gastos()
