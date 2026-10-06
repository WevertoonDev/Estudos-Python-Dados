#pratica 272 funçoes e organizaçao de codigo
def contar_positivos(lista):
    qtd = 0
    for numero in lista:
        if numero > 0:
            qtd = qtd + 1
    return qtd
def analisar_lista(lista):
    qtd = contar_positivos(lista)
    soma = 0
    maior = None
    for numero in lista:
        soma = soma + numero
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
    return qtd, soma, maior
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5]
    resultado = analisar_lista(lista)
    print(resultado)
except ValueError:
    print("Valores inválidos")