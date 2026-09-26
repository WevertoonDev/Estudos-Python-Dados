#pratica 183
def analisar_lista(lista):
    qtd = 0
    soma = 0
    for numero in lista:
        if numero > 10:
            qtd = qtd + 1
            soma = soma + numero
    return soma
resultado = analisar_lista(lista=[5, 12, 8, 20, 15, 3])
print(resultado)