# Demonstração do uso do método replace() em strings em Python

# Exemplo 1: Substituir uma substring por outra
texto = "A força eletromotriz induzida em qualquer circuito fechado"
resultado_1 = texto.replace("força", "bicicleta")
print("Exemplo 1 - Substituir substring")
print(f"Texto original: {texto}")
print(f"Texto modificado: {resultado_1}\n")

# Exemplo 2: Limitar o número de substituições
texto_2 = "banana, banana, banana"
resultado_2 = texto_2.replace("banana", "maçã", 2)
print("Exemplo 2 - Limitar o número de substituições a 2 ocorrências")
print(f"Texto original: {texto_2}")
print(f"Texto modificado: {resultado_2}\n")

#Exemplo 3: Inserir caractere antes de cada caractere (primeiro parametro vazio)
texto_3 = "ABCD"
resultado_3 = texto_3.replace("", "#")
print("Exemplo 3 - Inserir caractere antes de cada caractere")
print(f"Texto original: {texto_3}")
print(f"Texto modificado: {resultado_3}\n")

#Exemplo 4: Apagar um trecho do texto (substituir por string vazia)
texto_4 = "O rato roeu a roupa do rei de Roma"
resultado_4 = texto_4.replace("rato", "")
print("Exemplo 4 - Apagar um trecho do texto")
print(f"Texto original: {texto_4}")
print(f"Texto modificado: {resultado_4}\n")