#pratica 169
def analisar_vendas(lista):
    qtd = 0
    soma = 0
    maior = None
    menor = None
    for i in range(len(lista)):
        if lista[i] >= 2000:
            qtd = qtd + 1
            soma = soma + lista[i]
            if maior is None:
                maior = lista[i]
            elif lista[i] > maior:
                maior = lista[i]
            if menor is None:
                menor = lista[i]
            elif lista[i] < menor:
                menor = lista[i]
    media = soma / qtd
    return maior - menor
resultado = analisar_vendas([1500, 2200, 1800, 3000, 2500])
print(resultado)