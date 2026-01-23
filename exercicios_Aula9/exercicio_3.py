primos = []
lista = list(range(1,501))
for j in range(1,501):
    divisores = list(filter(lambda x: j%x == 0,lista))
    if len(divisores) <= 2:
        primos.append(j)

print(primos)