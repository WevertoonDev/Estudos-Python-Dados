#pratica 199
def calcular_media(lista):
    soma = 0
    for numero in lista:
        soma = soma + numero
    media = soma / len(lista)
    return media
def classificar_media(lista):
    media = calcular_media(lista)
    if media >= 8:
        return("Excelente")
    elif media >= 6:
        return("Bom")
    else:
        return("Precisa melhorar")
resultado = classificar_media(lista = [7, 8, 9, 6])
print(resultado)