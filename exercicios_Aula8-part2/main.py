def is_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def analise_Numero (numero,validacao):
    if validacao:
        if float(numero) <= 0:
            return "N"
        else:
            return "P"
    else:
        print(f"O digitado ({numero}) não é válido!")


while True:
    number = input("Digite um número: ")
    estado = analise_Numero(number,is_float(number))

    if estado == "P" or estado == "N":
        print(f"O estado do seu número é {estado}")
        break
    else:
        print("Redigite o número...")

