#pratica 174
def calcular_triplo(numero):
    return numero * 3
def classificar_triplo(numero):
    resultado = calcular_triplo(numero)
    if resultado >= 30:
        return("Alto")
    elif resultado >= 15:
        return("Médio")
    else:
        return("Baixo")
resultado = classificar_triplo(7)
print(resultado)