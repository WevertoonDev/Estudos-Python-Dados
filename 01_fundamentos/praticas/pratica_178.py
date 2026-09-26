#pratica 178
def calcular_triplo(numero):
    return numero * 3
def analisar_numero(numero):
    resultado = calcular_triplo(numero)
    if resultado >= 30:
        return("Alto")
    elif resultado>= 15:
        return("Médio")
    else:
        return("Baixo")
resultado = analisar_numero(8)
print(resultado)