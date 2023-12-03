from utils.limpar_console import limparConsole
from data.ler_dados import ler_dados

# Menu da funcionalidade 04 - Funcionalidade: Insights Financeiros
def menu_insights_financeiros():
    limparConsole(0)
    # saldo_total = ler_dados()
    # orçamento = ler_orcamento()
    from data.registros_categorias import registrosGerais
    orcamentoMensal = registrosGerais['orcamentoMensal']
    gastosTotais = 0
    for categoria in registrosGerais['categorias']:
        gastosTotais += float(categoria['gasto'])
    resto = (orcamentoMensal - gastosTotais)

    if(resto >= resto*1,10):
        print(f"Restou {resto} reais no seu orçamento.\n Você já pensou em investir?\n A opção mais conhecida é o Tesouro Selic, cuja rentabilidade segue de perto a variação dos juros e remunera 100% do CDI,\n ou seja, 13,65% ao ano atualmente. Este é um dos ativos mais populares, \npois possui liquidez diária e risco extremamente baixo – sendo indicado inclusive para a reserva de emergência.")
        limparConsole(4)
        from menu_principal import menu_principal
        menu_principal()
    else:
        print(f"Parece que você gastou mais que o seu orçamento. \n Só restou {resto} esse mês :(\n Já pensou em economizar as saídas no domingo?")
        limparConsole(3)
        from menu_principal import menu_principal
        menu_principal()
    # if saldo_total > orçamento:
    #     print("Parece que você gastou mais que o seu orçamento. Já pensou em economizar as saídas no domingo?")
    # else:
    #     print(
    #         "Ótimo! Você está dentro do orçamento. Já pensou em investir seu rico dinheirinho para render ainda mais?")

# Função: Ler e mostrar relatório de orçamento do usuário
# def ler_orcamento():
#     try:
#         with open("orçamento.txt", "r") as arquivo:
#             orçamento = float(arquivo.read())
#             return orçamento
#     except FileNotFoundError:
#         print("Arquivo de orçamento não encontrado. Defina um orçamento primeiro.")
#         return 0