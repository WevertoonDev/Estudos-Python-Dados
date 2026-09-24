#pratica 162
def calcular_menor(lista):
    menor = None
    for i in range(len(lista)):
        if menor is None:
            menor = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
    return menor
resultado = calcular_menor([18, 7, 25, 3, 12])
print(resultado)