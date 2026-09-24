#pratica 163
def calcular_soma_maiores(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] > 10:
            soma = soma + lista[i]
    return soma 
resultado = calcular_soma_maiores([5, 12, 8, 20, 15])
print(resultado)