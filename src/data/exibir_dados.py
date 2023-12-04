# Função para exibir todos os dados
def exibir_conteudo_arquivo():
    try:
        with open("registrosGerais.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")