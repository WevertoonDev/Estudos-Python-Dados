#pratica 184
def calcular_media_maiores(lista):
    soma = 0
    qtd = 0
    for numero in lista:
        if numero > 10:
            qtd = qtd + 1
            soma = soma + numero
    media = soma / qtd 
    return media 
resultado = calcular_media_maiores(lista=[5, 12, 8, 20, 15, 3])
print(resultado)