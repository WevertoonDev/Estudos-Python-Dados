#pratica 201
notas = [5, 8, 6, 9, 4, 7, 10]
def analisar_notas(lista):
    qtd = 0
    soma = 0
    maior = None
    menor = None
    for numero in lista:
        if numero >= 6:
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
    return qtd, soma, media, maior, menor
resultado = analisar_notas(notas)
print(resultado)