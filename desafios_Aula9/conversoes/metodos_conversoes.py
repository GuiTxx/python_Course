#funções com Celsius de partida
def celsius_fahren(t_celsius):
    return (t_celsius*1,8) + 32
def celsius_kelvin(t_celsius):
    return t_celsius+273.15

#funções com Fahrenheit de partida
def fahren_celsius(t_fahren):
    return (t_fahren-32)/1.8
def fahren_kelvin(t_fahren):
    return (t_fahren+459.67)/1.8

#funções com Kelvin de partida
def kelvin_celsius(t_kelvin):
    return t_kelvin-273.15
def kelvin_fahren(t_kelvin):
    return (t_kelvin*1.8) - 459.67

def calculo_funcoes(temperatura,indice):
    indice_int = int(indice)
    temp_float = float(temperatura)
    opcoes = {
        1 : lambda t: (t*1.8) + 32,
        2 : lambda t: t+273.15,
        3 : lambda t: (t-32)/1.8,
        4 : lambda t: (t+459.67)/1.8,
        5 : lambda t: t-273.15,
        6 : lambda t: (t*1.8) - 459.67
    }
    calculo_escolha = opcoes[indice_int](temp_float)
    return calculo_escolha