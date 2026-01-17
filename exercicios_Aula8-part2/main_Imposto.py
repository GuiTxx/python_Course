from somaImposto import calculo as cl

valor_prod = float(input("Informe o valor do Produto: "))
taxa = float(input("Informe a taxa em %: "))
valor_venda = cl.calc_Imposto(taxa,valor_prod)

print(f"O valor que eu devo vender meu produto é: {valor_venda:.2f}")
