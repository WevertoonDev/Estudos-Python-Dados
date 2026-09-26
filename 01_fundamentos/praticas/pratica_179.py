#pratica 179
def calcular_quadrado(numero):
    return numero * numero
def verificar_quadrado(nuemro):
    resultado = calcular_quadrado(nuemro)
    if resultado >= 100:
        return("Grande")
    elif resultado >= 50:
        return("Médio")
    else:
        return("Baixo")
resultado = verificar_quadrado(8)
print(resultado)