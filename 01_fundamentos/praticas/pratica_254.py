#pratica 254 
def analisar_lista(numeros):
    qtd = 0
    soma = 0
    qtd_n = 0
    maior = None
    for numero in numeros:
        if numero > 0:
            qtd = qtd + 1
            soma = soma + numero
        if numero < 0:
            qtd_n = qtd_n + 1
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
    return qtd, soma, qtd_n, maior
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4]
    resultado = analisar_lista(lista)
    print(resultado)
except:
    print("Valores inválidos")