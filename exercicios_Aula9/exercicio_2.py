from validacoes import metodos_validacao as val
User_numbers = []
for i in range(1,11):
    numero = float(input(f"Digite o {i}º número: "))
    val.validacao_float(numero)
    User_numbers.append(numero)
impares = list(filter(lambda x: x%2 != 0,User_numbers))
par = list(filter(lambda x: x%2 == 0, User_numbers))
print(f"Os números impares da lista são: {impares}\nOs números pares da lista são: {par}")
