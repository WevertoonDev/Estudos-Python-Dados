#pratica 188
def calcular_menor(lista):
    menor = None
    for numero in lista:
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
    return menor
def classificar_menor(lista):
    menor = calcular_menor(lista)
    if menor <10:
        return("Muito baixo")
    elif menor <20:
        return("Baixo")
    else:
        return("Normal")
resultado = classificar_menor(lista=[25, 12, 30, 18])
print(resultado)