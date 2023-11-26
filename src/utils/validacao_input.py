# Validação dos inputs
def input_valido(mensagem: object) -> object:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")