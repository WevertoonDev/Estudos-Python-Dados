#pratica 262 analise integrada de dados
def analisar_lista(numeros):
    qtd_p = 0
    qtd_n = 0
    soma_i = 0
    maior_p = None
    menor_n = None
    for numero in numeros:
        if numero > 0:
            qtd_p = qtd_p + 1
        if numero < 0:
            qtd_n = qtd_n + 1
            if menor_n is None:
                menor_n = numero
            elif numero < menor_n:
                menor_n = numero
        if numero % 2 == 0:
            if maior_p is None:
                maior_p = numero
            elif numero > maior_p:
                maior_p = numero
        else:
            soma_i = soma_i + numero
    return qtd_p, qtd_n,soma_i, maior_p, menor_n
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
except:
    print("Valores inválidos")