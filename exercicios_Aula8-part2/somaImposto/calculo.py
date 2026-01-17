def calc_Imposto(taxaImposto,custo):
    porcentagem = taxaImposto/100
    imposto = custo * porcentagem
    custo_new = imposto + custo
    return custo_new