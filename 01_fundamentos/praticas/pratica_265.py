#pratica 265
def analisar_pares(numeros):
    qtd_p = 0
    qtd_i = 0
    soma = 0
    maior = None
    for numero in numeros:
        if numero % 2 == 0:
            qtd_p = qtd_p + 1
            soma = soma + numero
        else:
            qtd_i = qtd_i + 1
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
    return qtd_p, qtd_i, soma, maior
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5]
    resultado = analisar_pares(lista)
    print(resultado)
except:
    print("Valores inválidos")