from time import sleep
# from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole
from data.registros_categorias import registrosGerais
# from data.salvar_dados import salvar_dados

# Menu da funcionalidade 02 - Funcionalidade: Inserir novo gasto
def menu_inserir_gasto():
    limparConsole()
    while True:
        if (len(registrosGerais['categorias'])>0):
            print('============================================================')
            print("As categorias que você definiu anteriormente foram:")
            for (categoria) in registrosGerais['categorias']:
                index = registrosGerais['categorias'].index(categoria)
                print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais.")
            print('============================================================')
            categoriaGasto = int(input("Digite o número da categoria que deseja adicionar a despesa: "))
            # for (categoria) in registrosGerais['categorias']:
            #     index = registrosGerais['categorias'].index(categoria)
            #     if (categoriaGasto in index):
            valorGasto = float(input("Digite o valor do gasto para ser adicionado a categoria escolhida: "))
            if (valorGasto < 1):
                raise ValueError("O valor do gasto não pode ser negativo.")
            else:
                registrosGerais['categorias'][categoriaGasto]['gasto'] = valorGasto
                print("Categoria atualizada com valor gasto.")
                print('============================================================')
                print("Agora suas categorias definidas estão atualizadas dessa forma:")
                for (categoria) in registrosGerais['categorias']:
                    index = registrosGerais['categorias'].index(categoria)
                    print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais. Você já gastou {categoria['gasto']} reais.")
                print('============================================================')
                sleep(2)
                limparConsole()
                break
        else:
            print("Ainda não existem categorias criadas, por favor, volte ao menu e crie novas categorias.")
            sleep(2)
            limparConsole()
            break
        # categorias = ler_categorias()
        # if not categorias:
        #     print("Nenhuma categoria encontrada. Adicione categorias primeiro.")
        #     break

        # print("\nInserir Novo Gasto")
        # for key, value in categorias.items():
        #     print(f"{key}. {value}")
        # print(f"{len(categorias) + 1}. Voltar ao Menu Principal")

        # escolha = input_valido("Escolha uma opção: ")

        # if escolha in categorias:
        #     try:
        #         gastos = float(input("Digite o valor do gasto: "))
        #         if gastos < 0:
        #             raise ValueError("O valor do gasto não pode ser negativo.")  # Para impedir o uso de valores negativos.

        #         categoria = categorias[escolha]
        #         salvar_dados(0, gastos, categoria)
        #     except ValueError as e:
        #         print(f"Erro: {e}. Por favor, insira um valor válido.")
        # elif escolha == len(categorias) + 1:
        #     break
        # else:
        #     print("Opção inválida, tente novamente.")

# Função: Mostrar categorias de gastos definidas pelo usuário
# def ler_categorias() -> object:
#     categorias = {}
#     try:
#         with open("categorias.txt", "rt") as arquivo:
#             for linha in arquivo:
#                 nome, _ = linha.strip().split(':')
#                 categorias[len(categorias) + 1] = nome
#     except FileNotFoundError:
#         print("Arquivo de categorias não encontrado.")
#     return categorias