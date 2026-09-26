def calcular_media(n1, n2, n3):
    soma = 0
    for numero in (n1, n2, n3):
        soma = soma + numero
    return soma / 3
resultado = calcular_media(8, 7,9)
print(resultado)