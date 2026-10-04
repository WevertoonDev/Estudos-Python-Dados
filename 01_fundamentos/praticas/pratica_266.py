#pratica 266
def contar_valores(numeros):
    qtd = 0
    qtd_n = 0
    qtd_i = 0
    soma = 0
    menor = None
    for numero in numeros:
        soma = soma + numero
        if numero > 0:
            qtd = qtd + 1
            if menor is None:
                menor = numero
            elif numero < menor:
                menor = numero
        elif numero < 0:
            qtd_n = qtd_n + 1
        else:
            qtd_i = qtd_i + 1
    return qtd, qtd_n, qtd_i, soma, menor
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    n6 = int(input("Digite um numero: "))
    n7 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5, n6, n7]
    resultado = contar_valores(lista)
    print(resultado)
except ValueError:
    print("Valores inválidos")
