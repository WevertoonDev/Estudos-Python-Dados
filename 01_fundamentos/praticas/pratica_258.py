#pratica 258 analise de uma lista 
def analisar_numero(numeros):
    qtd = 0
    qtd_b = 0
    qtd_i = 0
    soma = 0
    menor = None
    for numero in numeros:
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
        if numero > 10:
            qtd = qtd + 1
            soma = soma + numero
        elif numero < 10:
            qtd_b = qtd_b + 1
        else:
            qtd_i = qtd_i + 1
    return qtd, qtd_b, qtd_i, soma, menor
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5]
    resultado = analisar_numero(lista)
    print(resultado)
except:
    print("Valores inválidos")