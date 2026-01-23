def validacao_float(numero):
    try:
        teste = float(numero)
        return True
    except ValueError:
        print("Erro! Valor digitado não é numérico")
        return False