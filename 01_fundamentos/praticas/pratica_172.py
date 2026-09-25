#pratica 172
def calcular_dobro(numero):
    return numero * 2
def dobro_menos_cinco(numero):
    resultado = calcular_dobro(numero)
    return resultado - 5
resultado = dobro_menos_cinco(20)
print(resultado)