#pratica 195
def analisar_vendas(lista):
    maior = None
    menor = None
    soma = 0
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
        soma = soma + numero
    dif = maior - menor
    return dif
def classificar_vendas(lista):
    dif = analisar_vendas(lista)
    if dif >= 2000:
        return("Grande diferença")
    elif dif >= 1000:
        return("Diferença média")
    else:
        return("Pequena diferença")
resultado = classificar_vendas(lista=[1200, 2500, 1800, 3200, 2000])
print(resultado)