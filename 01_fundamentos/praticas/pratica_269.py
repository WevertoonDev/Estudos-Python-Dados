#pratica 269 desafio de consolidacao2/3
def analisar_lista(lista):
    qtd = 0
    qtd_i = 0
    soma = 0
    maior = None
    total = 0
    soma_t = 0
    for numero in lista:
        if numero > 0:
            total = total + 1
            soma_t = soma_t + numero
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if numero > 10:
            qtd = qtd + 1
        if numero <= 10:
            qtd_i = qtd_i + 1
        if numero % 2 == 0:
            soma = soma + numero
    if total > 0:
        media = soma_t / total
    else:
        media = None
    return qtd, qtd_i, soma, media, maior
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    n6 = int(input("Digite um numero: "))
    n7 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5, n6, n7]
    resultado = analisar_lista(lista)
    print(resultado)
except ValueError:
    print("Valores inválidos")