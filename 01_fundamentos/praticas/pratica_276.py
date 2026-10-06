#Pratica_276_Lista_Dicionários_e_Estruturas
def analisar_numeros(lista):
    qtd_p = 0
    qtd_n = 0
    soma_p = 0 
    soma_i = 0
    maior = None
    menor = None
    for numero in lista:
        if numero > 0:
            qtd_p = qtd_p + 1
        if numero < 0:
            qtd_n = qtd_n + 1
        if numero % 2 == 0:
            soma_p = soma_p + numero
        else:
            soma_i = soma_i + numero
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
    return qtd_p, qtd_n, soma_p, soma_i, maior, menor
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