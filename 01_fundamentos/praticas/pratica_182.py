#pratica 182
def calcular_soma_maiores(lista):
    soma = 0
    for numero in lista:
        if numero > 10:
            soma = soma + numero
    return soma
resultado = calcular_soma_maiores(lista=[5, 12, 8, 20, 15])
print(resultado)