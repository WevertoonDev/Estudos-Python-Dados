#pratica 175
def calcular_dobro(numero):
    return numero * 2
def analisar_numero(numero):
    resultado = calcular_dobro(numero)
    if resultado >= 40:
        return("Alto")
    elif resultado >= 20:
        return("Médio")
    else:
        return("Baixo")
resultado = analisar_numero(15)
print(resultado)