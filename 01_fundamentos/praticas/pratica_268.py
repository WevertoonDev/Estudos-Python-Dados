#Pratica 268
def analisar_numeros(numeros):
    qtd_p = 0
    qtd_n = 0
    soma = 0
    qtd_pa = 0
    maior = None
    for numero in numeros:
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if numero > 0:
            qtd_p = qtd_p + 1
        if numero < 0:
            qtd_n = qtd_n + 1
        if numero % 2 == 0:
            qtd_pa = qtd_pa + 1
        if numero / 3:
            soma = soma + numero
    return qtd_p, qtd_n, soma, qtd_pa, maior
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    n6 = int(input("Digite um numero: "))
    n7 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5, n6, n7]
    resultado = analisar_numeros(lista)
    print(resultado)
except ValueError:
    print("Valores inválidos")