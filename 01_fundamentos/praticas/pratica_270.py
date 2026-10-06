#pratica 270 desafio de consolidação
def analisar_numeros(lista):
    qtd_p = 0
    qtd_n = 0
    soma_p = 0
    soma_i = 0
    soma_t = 0 
    maior_p = None
    menor_i = None
    for numero in lista:
        if numero > 0:
            soma_t = soma_t + numero
            qtd_p = qtd_p + 1
            if numero % 2 == 0:
                soma_p = soma_p + numero
                if maior_p is None:
                    maior_p = numero
                elif numero > maior_p:
                    maior_p = numero
        if numero < 0:
            qtd_n = qtd_n + 1
            if numero % 2 == 1:
                soma_i = soma_i + numero
                if menor_i is None:
                    menor_i = numero
                elif numero < menor_i:
                    menor_i = numero
    if qtd_p > 0:
        media = soma_t / qtd_p
    else:
        media = None
    return qtd_p, qtd_n, soma_p, soma_i, maior_p, menor_i, media
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