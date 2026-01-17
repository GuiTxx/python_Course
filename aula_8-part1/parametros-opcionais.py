def soma(valor1, valor2, imprime=False):
    resultado = valor1 + valor2
    if imprime:
        print(f'Soma: {resultado}')
    return resultado
total = soma(10,84)
print(soma(valor2=20, imprime=True,valor1=30)) #Posicional explicita, mesmo que não siga a ordem do que foi declarado
print(total)