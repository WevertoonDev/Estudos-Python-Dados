#pratica 161 funcoes mais lista
def calcular_maior(lista):
    maior = None
    for i in range(len(lista)):
        if maior is None:
            maior = lista[i]
        elif lista[i] > maior:
            maior = lista[i]
    return maior
resultado = calcular_maior([12, 7, 25, 18, 9])
print(resultado)