#Pratica 194
def analisar_estoque(lista):
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
    media = soma / len(lista)
    return dif
def classificar_estoque(lista):
    dif = analisar_estoque(lista)
    if  dif >= 30:
        return("Grande variação")
    elif dif >= 15:
        return("Variação média")
    else:
        return("Pequena variação")
resultado = classificar_estoque(lista=[12, 25, 18, 40, 30])
print(resultado)