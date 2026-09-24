#pratica 159
def calcular_media(lista):
    soma = 0
    media = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    media = soma / len(lista)
    return media 
resultado = calcular_media([10, 20, 30, 40])
print(resultado)