#pratica 274 lista dicionario e estruturas
def analisar_lista(lista):
    qtd_p = 0
    qtd_i = 0
    soma = 0
    maior = None
    menor = None
    for numero in lista:
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
        if numero % 2 == 0:
            qtd_p = qtd_p + 1
        else:
            qtd_i = qtd_i + 1
        if numero > 0:
            soma = soma + numero
    return qtd_p, qtd_i, soma, maior, menor
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