# Fazer leitura de arquivo
registrosGerais = {
    'orcamentoMensal': 1200,
    'categorias' : [{{'nome': 'saude', 'limite': 200, 'gasto': 0}}, {{'nome': 'educacao', 'limite': 200, 'gasto': 0}}]
}
# Deve salvar no arquivo de texto o orcamentoMensal primeiro sendo separado por virgula
# ex.: orcamentoMensal, 1200
# Já as categorias vai acontecer da mesma forma mas, como cada uma delas é um dicionario será necessário apenas ser salvo o valor e não a chave
# ex.: saude, 200, 0
# Ao final, deve ter no arquivo de texto uma linha para cada um. A ação que está sendo feita é para salvar os valores do usuário utilizados no dicionario 
# para depois manter salvo e sendo usado na aplicação. 

# Fazer as ações de ler e escrever no arquivo