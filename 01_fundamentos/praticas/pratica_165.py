#Pratica_165
def analisar_lista(lista):
    qtd = 0
    soma = 0
    maior = None
    for i in range(len(lista)):
        if lista[i] > 10:
            qtd = qtd + 1
            soma = soma + lista[i]
    media = soma / qtd
    for i in range(len(lista)):
        if lista[i] > 10:
            if maior is None:
                maior = lista[i]
            elif lista[i] > maior:
                maior = lista[i]
    return media 
resultado = analisar_lista([5, 12, 8, 20, 15, 30])
print(resultado)