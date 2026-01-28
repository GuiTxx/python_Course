dataNasci = input("Digite sua data de nascimento(separe por .): ")
dataCerta = dataNasci.replace(".","/")
months = [{"01":"Janeiro"},
          {"02":"Fevereiro"},
          {"03":"Março"},
          {"04":"Abril"},
          {"05":"Maio"},
          {"06":"Junho"},
          {"07":"Julho"},
          {"08":"Agosto"},
          {"09":"Setembro"},
          {"10":"Outubro"},
          {"11":"Novembro"},
          {"12":"Dezembro"}]
mes_Aniver = dataCerta[3:5]
for month in months:
    if mes_Aniver in month:
        print(f"Você nasceu em {dataCerta[0:2]} de {month[mes_Aniver]} de {dataCerta[6:10]}")
