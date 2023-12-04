# Função para salvar os dados do dicionário ao finalizar programa
def salvar_dicionario(registros):
    with open("registrosGerais.txt", "w") as arquivo:
        linhaOrcamento = f"{registros['orcamentoMensal']}\n"
        arquivo.write(linhaOrcamento)
        categorias = registros['categorias']
        for categoria in categorias:
            linha = f"{categoria['nome']},{categoria['limite']},{categoria['gasto']}\n"
            arquivo.write(linha)