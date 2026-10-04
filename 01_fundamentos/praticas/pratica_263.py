#pratica 263 avaliacao final
def  analisar_numeros(numeros):
    qtd_p = 0
    qtd_n = 0
    soma_p = 0
    qtd_i = 0
    menor = None
    for numero in numeros:
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
        if numero > 0:
            qtd_p = qtd_p + 1
        if numero < 0:
            qtd_n = qtd_n + 1
        if numero % 2 == 0:
            soma_p = soma_p + numero
        else:
            qtd_i = qtd_i + 1
    return qtd_p, qtd_n, soma_p, qtd_i, menor
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    n6 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5, n6]
    resultado = analisar_numeros(lista)
    print(resultado)
except:
    print("Valores inválidos")