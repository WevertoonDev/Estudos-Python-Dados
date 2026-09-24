#pratica 168
def analisar_vendas(lista):
    qtd = 0
    soma = 0
    maior = None
    for i in range(len(lista)):
        if lista[i] >= 2000:
            qtd = qtd + 1
            soma = soma + lista[i]
    media = soma / qtd
    for i in range(len(lista)):
        if lista[i] >= 2000:
            if maior is None:
                maior = lista[i]
            elif lista[i] > maior:
                maior = lista[i]
    return maior
resultado = analisar_vendas([1500, 2200, 1800, 3000, 2500])
print(resultado)