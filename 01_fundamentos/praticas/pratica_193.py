#pratica 193
def analisar_notas(lista):
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
def classificar_diferenca_notas(lista):
    dif = analisar_notas(lista)
    if dif >= 5:
        return("Grande variação")
    elif dif >= 3:
        return("Variação média")
    else:
        return("Pequena variação")
resultado = classificar_diferenca_notas(lista=[6, 8, 7, 10, 9])
print(resultado)