def soma(n1,n2):
    soma_result = n1+n2
    return soma_result
def subtracao(n1,n2):
    if n1 > n2:
        sub = n1-n2
    else:
        sub = n2-n1
    return sub
print('Bem vindo a calculadora')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
op = int(input('Digite 1 para somar e 2 para subtrair'))

if op == 1:
    print(f"O valor da soma {num1} e {num2} é {soma(num1,num2)}")
elif op == 2:
    print(f"O valor da subtração {num1} e {num2} é {subtracao(num1, num2)}")
else:
    print('Comando inválido!!')