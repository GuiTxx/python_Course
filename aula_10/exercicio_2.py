frase = input("Digite uma frase aleatória: ")
frase_Analise = frase.lower()
espacos = frase_Analise.count(" ")
vogal_a = frase_Analise.count("a")
vogal_e = frase_Analise.count("e")
vogal_i = frase_Analise.count("i")
vogal_o = frase_Analise.count("o")
vogal_u = frase_Analise.count("u")

print(f"Nesta frase nós temos\nEspaços: {espacos}\nVogal (a): {vogal_a}\n"
      f"Vogal (e): {vogal_e}\nVogal (i): {vogal_i}\nVogal (o): {vogal_o}\n"
      f"Vogal (u): {vogal_u}")