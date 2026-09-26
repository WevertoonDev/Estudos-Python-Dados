#pratica 187
def calcular_maior(lista):
    maior = None
    for numero in lista:
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
    return maior
def classificar_maior(lista):
    maior = calcular_maior(lista)
    if maior >= 100:
        return("Muito alto")
    elif maior >= 50:
        return("Alto")
    else:
        return("Baixo")
resultado = classificar_maior(lista=[20, 75, 40, 60])
print(resultado)