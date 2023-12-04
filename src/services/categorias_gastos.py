from time import sleep
from utils.validacao_input import input_valido
from utils.limpar_console import limparConsole
from data.registros_categorias import registrosGerais
from utils.mensagem import layoutMensagem

# Menu da funcionalidade 01 - Funcionalidade: Definir categorias de gasto
def menu_definir_categorias():
    layoutMensagem("Olá, seja bem-vindo a nossa funcionalidade de definição de categorias de despesas e seus limites de gasto!\nNesta funcionalidade você poderá definir e editar essas categorias de forma altamente personalizada \nse adequando assim a sua forma de gerir o seu rico dinheirinho.\nAproveite ;)")
    print("Menu de Categorias\n 1. Definir Orçamento Total Mensal\n 2. Editar Orçamento Total Mensal\n 3. Criar Categorias de Despesas\n 4. Editar Categorias de Despesas\n 5. Deletar categoria de gasto \n 6. Visualizar orçamento total e categorias \n 7. Voltar ao Menu Principal")
    escolha = input_valido("Escolha uma opção: ")

    if escolha == 1:
        limparConsole(0)
        definir_orcamento()
    elif escolha == 2:
        limparConsole(0)
        editar_orcamento()
    elif escolha == 3:
        limparConsole(0)
        criar_categoria()
    elif escolha == 4:
        limparConsole(0)
        editar_categoria()
    elif escolha == 5:
        limparConsole(0)
        deletarCategoria()
    elif escolha == 6:
        limparConsole(0)
        visualizarDados()
    elif escolha == 7:
        from menu_principal import menu_principal
        limparConsole(0)
        menu_principal()
    else:
        print("Opção inválida, tente novamente.")
        limparConsole(1)
# Função: Definir orçamento mensal total
def definir_orcamento():
    try:
        orcamento = float(input("Digite o valor do orçamento total mensal: "))
        registrosGerais['orcamentoMensal'] = orcamento
        print("Orçamento definido com sucesso.")
        limparConsole(2)
        menu_definir_categorias()
    except ValueError:
        print("Por favor, insira um número válido.")
        limparConsole(2)


# Função: Editar orçamento mensal total 
def editar_orcamento():
    try:
        layoutMensagem(f"O seu orçamento anterior estava definido no valor de {registrosGerais['orcamentoMensal']}")
        novo_orcamento = float(input("Digite o novo valor do orçamento: "))
        registrosGerais['orcamentoMensal'] = novo_orcamento
        print("Orçamento atualizado com sucesso.")
        limparConsole(2)
        menu_definir_categorias()


    except FileNotFoundError:
        print("Orçamento não definido. Defina um orçamento primeiro.")
        limparConsole(2)
        menu_definir_categorias()
    except ValueError:
        print("Por favor, insira um número válido.")
        limparConsole(2)

# Função: Criar nova categoria de gasto
def criar_categoria():
    nova_categoria = input("Digite o nome da nova categoria de despesa que você deseja criar: ")
    limite = float(input("Defina um limite para gastos com esta categoria: "))
    gasto = 0
    registrosGerais['categorias'].append({'nome':nova_categoria, 'limite': limite, 'gasto': gasto})
    print("Categoria criada com sucesso.")
    limparConsole(2)
    continuar = input("Deseja continuar e criar mais categorias? Você pode responder com S para sim e N para não ;)\n").upper()
    if (continuar == 'S'):
        limparConsole(0)
        print('============================================================')
        print("As categorias que você criou até agora são:")
        for (categoria) in registrosGerais['categorias']:
            index = registrosGerais['categorias'].index(categoria)
            print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais.")
        print('============================================================')
        criar_categoria()
    else:
        menu_definir_categorias()

# Função: Editar categoria de gastos   
def editar_categoria():
    try:
        print('============================================================')
        print("As categorias que você definiu anteriormente foram:")
        for (categoria) in registrosGerais['categorias']:
            index = registrosGerais['categorias'].index(categoria)
            print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais.")
        print('============================================================')
        categoriaEditar = int(input("Digite o número da categoria que deseja editar: "))
        novoNome = input(f"Digite um novo nome para esta categoria: ")
        novoLimite = float(input("Defina o novo limite de gastos para esta categoria: "))
        registrosGerais['categorias'][categoriaEditar]['nome'] = novoNome
        registrosGerais['categorias'][categoriaEditar]['limite'] = novoLimite
        print('Categoria editada com sucesso.')
        continuar = input("Deseja continuar e criar mais categorias? Você pode responder com S para sim e N para não ;)\n").upper()
        limparConsole(0)
        while (continuar == 'S'):
            limparConsole(0)
            editar_categoria()
        else:
            limparConsole(0)
            menu_definir_categorias()
    except FileNotFoundError:
        print("Nenhum dado de gasto encontrado.")
        sleep(1)
        menu_definir_categorias()
    print("Categoria editada com sucesso.")
    limparConsole(1)

def deletarCategoria():
    print('============================================================')
    print("As categorias que você definiu anteriormente foram:")
    for (categoria) in registrosGerais['categorias']:
        index = registrosGerais['categorias'].index(categoria)
        print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais.")
    print('============================================================')
    categoriaDeletar = int(input("Digite o número da categoria que deseja deletar: "))
    registrosGerais['categorias'].pop(categoriaDeletar)
    print("Categoria deletada com sucesso.")
    limparConsole(1)
    menu_definir_categorias()


def visualizarDados():
    print('============================================================')
    print(f"O seu orçamento mensal atualizado está no valor de {registrosGerais['orcamentoMensal']}.")
    print("As categorias que você definiu foram:")
    for (categoria) in registrosGerais['categorias']:
        index = registrosGerais['categorias'].index(categoria)
        print(f"{index}.{categoria['nome']} com limite de {categoria['limite']} reais.")
    print('============================================================')    
    voltar = int(input("Digite 1 para voltar ao menu das categorias de despesa ;)\n"))
    if(voltar == 1):
        menu_definir_categorias()
    else:
        print("Digite uma opção válida.")
    limparConsole(3)
