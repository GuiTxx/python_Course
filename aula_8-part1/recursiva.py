def fatorial(numero):
    if type(numero) is not int:
        return '\n O número deve ser um inteiro'
    if numero <= 0:
        return 1
    else:
        return  numero * fatorial(numero-1)
x = int(input('Digite um número para a operação fatorial: '))
print(fatorial(x))