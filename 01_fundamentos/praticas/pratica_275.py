#pratica 275 
def comparar_listas(lista1, lista2):
    indice = 0
    qtd = 0
    qtd_d = 0
    soma_p = 0
    soma_s = 0
    maior = None
    for numero in lista1:
        if numero == lista2[indice]:
            qtd = qtd + 1
        else:
            qtd_d = qtd_d + 1
        soma_p = soma_p + numero
        soma_s = soma_s + lista2[indice]
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if maior is None:
            maior = lista2[indice]
        elif lista2[indice] > maior:
            maior = lista2[indice]
        indice = indice + 1
    return qtd, qtd_d, soma_p, soma_s, maior
lista1 = [5, 8, 3, 10]
lista2 = [5, 2, 3, 7]

resultado = comparar_listas(lista1, lista2)
print(resultado)