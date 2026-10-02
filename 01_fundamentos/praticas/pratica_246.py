#pratica 246
def analisar_numeros(numeros):
    qtd = 0
    soma = 0
    maior = None
    menor = None
    qtd_m = 0
    qtd_i = 0
    qtd_n = 0
    qtd_p = 0
    for numero in numeros:
        if numero > 10:
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
        if numero <= 10:
            qtd_m = qtd_m + 1
        if numero == 10:
            qtd_i = qtd_i + 1
        if numero < 0:
            qtd_n = qtd_n + 1
        if numero % 2 == 0:
            qtd_p = qtd_p + 1
    if qtd == 0:
        return 0, 0, 0, 0, 0, qtd_m, qtd_i, qtd_n, qtd_p
    media = soma / qtd
    return qtd, soma, media, maior, menor, qtd_m, qtd_i, qtd_n, qtd_p
try:
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um numero: "))
    n3 = float(input("Digite um numero: "))
    n4 = float(input("Digite um numero: "))
    lista = [n1, n2, n3, n4]
    resultado = analisar_numeros(lista)
    print(resultado)
except:
    print("Valores inválidos")