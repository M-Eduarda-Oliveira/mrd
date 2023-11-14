import os

os.system('cls')

caminho_percorrido = ["MENU INICIAL"]

menu_INICIAL = ["DEFINIR GASTOS", "INSERIR NOVO GASTO", "RELATÓRIO DE GASTOS", "EDUCAÇÃO FINANCEIRA"]
menu_DEFINIR_GASTOS = ["DEFINIR GASTOS"]
menu_INSERIR_NOVO_GASTO = ["INSERIR NOVO GASTO"]
menu_RELATORIO_DE_GASTOS = ["RELATÓRIO DE GASTOS"]
menu_EDUCACAO_FINANCEIRA = ["EDUCAÇÃO FINANCEIRA"]

def tamanho_identacao():
    tamanho_identacao = 0
    identacao = ""    
    for i, m in enumerate(caminho_percorrido):
        tamanho_identacao = tamanho_identacao + len(caminho_percorrido[i])
    tamanho_identacao = (tamanho_identacao - len(caminho_percorrido[-1]) + 4)
    for i in range(tamanho_identacao):
        identacao = identacao + " "
    return identacao

def exibir_menus():

    if caminho_percorrido[-1] == "MENU INICIAL":
        print(f"{caminho_percorrido[0]}\n")    
        for i, m in enumerate(menu_INICIAL):
            print(f"[{i+1}] - [{m}]")
        print("-")
        print("[0] - SAIR\n")
        opcao = int(input(">> "))
        if opcao == 0:
            os.system('cls')
            print("\nObrigado por utilizar o MRD.\n")
            return "SAIR"
        else:
            caminho_percorrido.append(menu_INICIAL[opcao-1])

    elif len(caminho_percorrido) == 2:
        os.system('cls')
        if caminho_percorrido[-1] == "DEFINIR GASTOS":
            print(f"{' >> '.join(caminho_percorrido)}\n")
            identacao = tamanho_identacao()
            for i, m in enumerate(menu_DEFINIR_GASTOS):
                print(f"{identacao}[{i+1}] - [{m}]")
            print(f"{identacao} -")
            print(f"{identacao}[{len(menu_DEFINIR_GASTOS)+1}] - VOLTAR")
            print(f"{identacao}[0] - SAIR\n")
            opcao = int(input(">> "))
            if opcao == 0:
                os.system('cls')
                print("\nObrigado por utilizar o MRD.\n")
                return "SAIR"
            elif opcao == len(menu_DEFINIR_GASTOS) + 1:
                os.system('cls')
                caminho_percorrido.pop()        
            else:
                caminho_percorrido.append(menu_DEFINIR_GASTOS[opcao-1])
                #chama função para O CRUD

        elif caminho_percorrido[-1] == "INSERIR NOVO GASTO":
            print(f"{' >> '.join(caminho_percorrido)}\n")
            identacao = tamanho_identacao()
            for i, m in enumerate(menu_INSERIR_NOVO_GASTO):
                print(f"{identacao}[{i+1}] - [{m}]")
            print(f"{identacao} -")
            print(f"{identacao}[{len(menu_INSERIR_NOVO_GASTO)+1}] - VOLTAR")
            print(f"{identacao}[0] - SAIR\n")
            opcao = int(input(">> "))
            if opcao == 0:
                os.system('cls')
                print("\nObrigado por utilizar o MRD.\n")
                return "SAIR"
            elif opcao == len(menu_INSERIR_NOVO_GASTO) + 1:
                os.system('cls')
                caminho_percorrido.pop()        
            else:
                caminho_percorrido.append(menu_INSERIR_NOVO_GASTO[opcao-1])
                #chama função para O CRUD

        elif caminho_percorrido[-1] == "RELATÓRIO DE GASTOS":
            print(f"{' >> '.join(caminho_percorrido)}\n")
            identacao = tamanho_identacao()
            for i, m in enumerate(menu_RELATORIO_DE_GASTOS):
                print(f"{identacao}[{i+1}] - [{m}]")
            print(f"{identacao} -")
            print(f"{identacao}[{len(menu_RELATORIO_DE_GASTOS)+1}] - VOLTAR")
            print(f"{identacao}[0] - SAIR\n")
            opcao = int(input(">> "))
            if opcao == 0:
                os.system('cls')
                print("\nObrigado por utilizar o MRD.\n")
                return "SAIR"
            elif opcao == len(menu_RELATORIO_DE_GASTOS) + 1:
                os.system('cls')
                caminho_percorrido.pop()        
            else:
                caminho_percorrido.append(menu_RELATORIO_DE_GASTOS[opcao-1])
                #chama função para O CRUD
        
        elif caminho_percorrido[-1] == "EDUCAÇÃO FINANCEIRA":
            print(f"{' >> '.join(caminho_percorrido)}\n")
            identacao = tamanho_identacao()
            for i, m in enumerate(menu_EDUCACAO_FINANCEIRA):
                print(f"{identacao}[{i+1}] - [{m}]")
            print(f"{identacao} -")
            print(f"{identacao}[{len(menu_EDUCACAO_FINANCEIRA)+1}] - VOLTAR")
            print(f"{identacao}[0] - SAIR\n")
            opcao = int(input(">> "))
            if opcao == 0:
                os.system('cls')
                print("\nObrigado por utilizar o MRD.\n")
                return "SAIR"
            elif opcao == len(menu_EDUCACAO_FINANCEIRA) + 1:
                os.system('cls')
                caminho_percorrido.pop()        
            else:
                caminho_percorrido.append(menu_EDUCACAO_FINANCEIRA[opcao-1])
                #chama função para O CRUD
                
while True:

    if exibir_menus() == "SAIR":
        break
    
    
        


    