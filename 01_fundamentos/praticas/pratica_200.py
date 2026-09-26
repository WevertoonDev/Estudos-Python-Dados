#pratica 200
vendas = [1200, 2500, 1800, 3200, 2700, 1500, 4100]
def analisar_vendas(lista):
    qtd = 0
    soma = 0
    maior = None
    menor = None
    for numero in lista:
        if numero >= 2000:
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
resultado = analisar_vendas(vendas)
print(resultado)