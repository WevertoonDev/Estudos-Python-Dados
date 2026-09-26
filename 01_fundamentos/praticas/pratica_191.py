#pratica 191
def analisar_precos(lista):
    maior = None
    menor = None
    soma = 0
    dif = None
    for numero in lista:
        soma = soma + numero
        if maior is None:
            maior = numero 
        elif numero > maior:
            maior = numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
    media = soma / len(lista)
    dif = maior - menor
    return dif
def classificar_precos(lista):
    dif = analisar_precos(lista)
    if dif >= 50 :
        return("Grande diferença")
    elif dif >= 20 :
        return("Diferença média")
    else:
        return("Pequena diferença")
resultado = classificar_precos(lista=[30, 80, 50, 60, 40])
print(resultado)