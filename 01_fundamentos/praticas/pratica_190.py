#Pratica_190
def analisar_numeros(lista):
    maior = None
    menor = None
    soma = 0
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
    media = soma / len(lista)
    return maior
def classificar_maior(lista):
    maior = analisar_numeros(lista)
    if maior >= 90:
        return("Excelente")
    elif maior >= 70:
        return("Bom")
    else:
        return("Baixo")
resultado = classificar_maior(lista=[65, 80, 72, 95, 60])
print(resultado)