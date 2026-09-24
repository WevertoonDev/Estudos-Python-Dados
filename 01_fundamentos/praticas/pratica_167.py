#pratica 167
def calcular_media_vendas(lista):
    qtd = 0
    soma = 0
    for i in range(len(lista)):
        if lista[i] >= 2000:
            qtd = qtd + 1
            soma = soma + lista[i]
    media = soma / qtd
    return media
resultado = calcular_media_vendas([1500, 2200, 1800, 3000, 2500])
print(resultado)