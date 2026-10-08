#pratica 277 
def analisar_lista(numeros):
    qtd = 0
    soma = 0
    maior = None
    menor = None
    for numero in numeros:
            qtd = qtd + 1
            soma = soma + numero
            if maior is None:
                maior = numero
            elif numero > maior:
                maior = numero
            if menor is None:
                menor = numero
            elif numero < menor:
                menor = numero
    media = soma / qtd
    resultado = {"quantidade": qtd,
                 "soma": soma,
                 "maior": maior,
                 "menor": menor,
                 "media": media}
    return resultado
numeros = [10, 5, 8, 2]
resultado = analisar_lista(numeros)
print(resultado)