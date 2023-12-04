# Função para carregar os dados salvos no dicionário
def carregar_dicionario(registros):
    registrosCategorias = registros['categorias']
    try:
        with open("registrosGerais.txt", "r") as arquivo:
            orcamentoMensal = arquivo.readline()
            registros['orcamentoMensal'] = float(orcamentoMensal)
            for linha in arquivo:
                nome, limite, gasto = linha.strip().split(',')
                registrosCategorias.append({
                    'nome': nome,
                    'limite': float(limite),
                    'gasto': float(gasto)
                })
        return registrosCategorias
    except FileNotFoundError:
        return []

