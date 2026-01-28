ddd = input("Digite o seu DDD: ")
num_Telefone = input("Digite o número de telefone: ")
num_Ajustado = num_Telefone.replace("-","")
if len(num_Telefone) <= 8:
    num_Certo ="9" + num_Ajustado
    print(num_Certo)
    print(f"({ddd}){num_Certo[0:5]}-{num_Certo[5:9]}")
else:
    print(f"({ddd}){num_Ajustado[0:5]}-{num_Ajustado[5:12]}")