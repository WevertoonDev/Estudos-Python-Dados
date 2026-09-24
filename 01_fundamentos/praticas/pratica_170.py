#Pratica_170_função_+_Lista_+_Múltiplas_Informaçoes
def analisar_vendas(lista):
    qtd = 0
    soma = 0
    maior = None
    menor = None
    dif = None
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
    dif = maior - menor
    return media
resultado = analisar_vendas([1200, 2500, 1800, 3200, 2100, 900, 2800])
print(resultado)