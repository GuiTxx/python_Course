def valorPagamento(valor_Cheio,dias_Atraso):
    if valor_Cheio > 0 and dias_Atraso == 0:
        return valor_Cheio
    elif valor_Cheio > 0 and dias_Atraso > 0:
        multa = 3/100
        juros = 0.1 / 100
        valor_Multa = valor_Cheio * multa
        valor_Juros = valor_Cheio*juros*dias_Atraso
        total_Valor = valor_Cheio+valor_Multa+valor_Juros
        return total_Valor

while True:
    i = 0
    prestacao_Valor = float(input("Digite o valor da prestação: "))
    if prestacao_Valor == 0:
        break
    elif prestacao_Valor < 0:
        print("O valor da prestação não pode ser negativo.")
        continue
    else:
        dias_Atraso = int(input("Dias de atraso: "))
        valor_Prestacao = valorPagamento(prestacao_Valor,dias_Atraso)
        i += 1
        print(f"Sua {i}º prestação foi reajustada para -> {valor_Prestacao}")
        print(f"Calcule a {i+1}º prestação...")

