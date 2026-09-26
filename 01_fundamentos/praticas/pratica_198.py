#pratica 198
numeros = [12, 7, 25, 18, 30, 9]

def calcular_maior(lista):

    maior = None

    for numero in lista:
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero

    return maior

resultado = calcular_maior(numeros)

print(resultado)
#pratica 198.2 
numeros = [12, 7, 25, 18, 30, 9]
def calcular_maior(lista):
    maior = None
    for numero in lista:
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
    return maior
resultado = calcular_maior(numeros)
print(resultado)