#pratica 259 análise de numeros pares e impares
def analisar_lista(numeros):
    qtd_p = 0
    qtd_i = 0
    soma_p = 0
    soma_i = 0
    menor = None
    for numero in numeros:
        if numero % 2 == 0:
            qtd_p = qtd_p + 1
            soma_p = soma_p + numero
        else:
            qtd_i = qtd_i + 1
            soma_i = soma_i + numero
            if menor is None:
                menor = numero
            elif numero < menor:
                menor = numero
    return qtd_p, qtd_i, soma_p, soma_i, menor
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