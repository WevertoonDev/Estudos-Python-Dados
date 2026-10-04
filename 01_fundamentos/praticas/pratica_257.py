#pratica 257 Classificação e análise de uma lista 
def analisar_lista(numeros):
    qtd_p = 0
    qtd_n = 0
    qtd_z = 0
    soma_p = 0
    maior_n = None
    for numero in numeros:
        if numero > 0:
            qtd_p = qtd_p + 1
            soma_p = soma_p + numero
        elif numero < 0:
            qtd_n = qtd_n + 1
            if maior_n is None:
                maior_n = numero
            elif numero > maior_n:
                maior_n = numero
        else:
            qtd_z = qtd_z + 1
    return qtd_p, qtd_n, qtd_z, soma_p, maior_n
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5]
    resultado = analisar_lista(lista)
    print(resultado)
except:
    print("Valores inválidos")