#pratica 164
def calcular_media_maiores(lista):
    soma = 0
    qtd = 0
    for i in range(len(lista)):
        if lista[i] > 10:
            qtd = qtd + 1
            soma = soma + lista[i]
    media = soma / qtd
    return media 
resultado = calcular_media_maiores([5, 12, 8, 20, 15])
print(resultado)