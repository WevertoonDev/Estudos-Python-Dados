#Pratica_273_Funções_e_Organização_de_Código
def somar_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma = soma + numero
    return soma
def analisar_lista(lista):
    soma = somar_pares(lista)
    qtd_n = 0
    menor = None
    qtd_p = 0
    total = 0
    for numero in lista:
        if numero > 0:
            qtd_p = qtd_p + 1
            total = total + numero
        if numero < 0:
            qtd_n = qtd_n + 1
            if menor is None:
                menor = numero
            elif numero < menor:
                menor = numero
    if qtd_p > 0:
        media = total / qtd_p
    else:
        media = None
    return soma, qtd_n, menor, media
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