from time import sleep
from utils.limpar_console import limparConsole
from data.registros_categorias import registrosGerais

# Função para inserir gasto
def menu_inserir_gasto():
    limparConsole(0)
    while True:
        if (len(registrosGerais['categorias'])>0):
            print('============================================================')
            print("As categorias que você definiu anteriormente foram:")
            for (categoria) in registrosGerais['categorias']:
                index = registrosGerais['categorias'].index(categoria)
                print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais.")
            print('============================================================')
            categoriaGasto = int(input("Digite o número da categoria que deseja adicionar a despesa: "))
            if (categoriaGasto in range (len(registrosGerais['categorias']))):
                valorGasto = float(input("Digite o valor do gasto para ser adicionado a categoria escolhida: ")) 
                registrosGerais['categorias'][categoriaGasto]['gasto'] = float(registrosGerais['categorias'][categoriaGasto]['gasto']) + valorGasto
                print("Categoria atualizada com valor gasto.")
                print('============================================================')
                limparConsole(2)
                print('============================================================')
                print("Agora suas categorias definidas estão atualizadas dessa forma:")
                for (categoria) in registrosGerais['categorias']:
                    index = registrosGerais['categorias'].index(categoria)
                    print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais. Você já gastou {categoria['gasto']} reais.")
                print('============================================================')
                limparConsole(3)
                from menu_principal import menu_principal
                menu_principal()
            else:
                print("Essa categoria não existe. Por favor verifique o número e tente novamento")  
                limparConsole(1)
                menu_inserir_gasto()
        else:
            print("Ainda não existem categorias criadas, por favor, volte ao menu e crie novas categorias.")
            limparConsole(3)
            break