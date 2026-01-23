from conversoes import metodos_conversoes as conv
from validacoes import metodos_validacao as val

texto_User = ("======Opções de Conversão======="
              "\n1-Celsius -> Fahrenheit\n2-Celsius -> Kelvin"
              "\n3-Fahrenheit -> Celsius\n4-Fahrenheit -> Kelvin"
              "\n5-Kelvin -> Celsius\n6-Kelvin -> Fahrenheit"
              "\n7-Finalizar")

while True:
    print(texto_User)
    escolha_Conversao = input("\n\nDigite o sistema de conversão desejado: ")
    if val.validacao_int(escolha_Conversao) != True:
        continue
    elif val.validacao_Intervalar(1,7,escolha_Conversao):
        continue
    elif int(escolha_Conversao) == 7:
        break

    while True:
        print("\nDeseja continuar? \n1- Sim\n2- Voltar")
        confirmacao = input("\nEscolha: ")

        if val.validacao_int(confirmacao) != True:
            continue
        elif val.validacao_Intervalar(1,2,confirmacao):
            continue
        elif int(confirmacao) == 2:
            break

        while True:
            valor_Temperatura = input("\nDigite o valor da Temperatura: ")
            if val.validacao_float(valor_Temperatura) != True:
                continue
            resultado = conv.calculo_funcoes(valor_Temperatura,escolha_Conversao)
            print(f"A conversão foi feita com sucesso!\n\nResultado: {resultado}")
            break
            # Eu ia fazer um monte de elif com as conts em cada um, com cada variavel diferente...



