#pratica 158 funcao mais lista mais filtro
def filtrar_maiores(lista):
    qtd = 0
    for i in range(len(lista)):
        if lista[i] > 10:
            qtd = qtd + 1
    return qtd
resultado = filtrar_maiores([5, 12, 8, 20, 15])
print(resultado)