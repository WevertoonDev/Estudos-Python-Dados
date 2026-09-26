#pratica 176
def calcular_dobro(numero):
    return numero * 2
def classificar_numero(numero):
    resultado = calcular_dobro(numero)
    if resultado >= 20:
        return("Alto")
    elif resultado >= 10:
        return("Médio")
    else:
        return("Baixo")
resultado = classificar_numero(6)
print(resultado)