#pratica 192
def analisar_salarios(lista):
    maior = None
    menor = None
    dif = None
    for numero in lista:
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
    dif = maior - menor
    return dif
def classificar_diferenca(lista):
    dif = analisar_salarios(lista)
    if dif >= 3000:
        return("Diferença alta")
    elif dif >= 1500:
        return("Diferença média")
    else:
        return("Diferença baixa")
resultado = classificar_diferenca(lista=[2500, 4200, 3100, 6000, 3500])
print(resultado)