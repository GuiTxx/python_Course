def validacao_float(numero):
    try:
        teste = float(numero)
        return True
    except ValueError:
        print("Erro! Valor digitado não é numérico")
        return False
def validacao_int(numero):
    if numero.isdigit():
        return True
    else:
        return False

def validacao_Intervalar(nao_ser_menor_que,nao_ser_maior_que,val):
    valor = int(val)
    if valor < nao_ser_menor_que or valor > nao_ser_maior_que:
        print("Erro! Valor digitado não é uma das opções.")
        return True
    elif valor > nao_ser_menor_que and valor < nao_ser_maior_que:
        return False
