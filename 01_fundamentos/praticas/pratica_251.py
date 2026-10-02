#pratica 251
def analisar_lista(numeros):
    qtd_p = 0
    qtd_i = 0
    soma_p = 0
    soma_i = 0
    qtd = 0
    for numero in numeros:
        if numero % 2 == 0:
            qtd_p = qtd_p + 1
            soma_p = soma_p + numero
        else:
            qtd_i = qtd_i + 1
            soma_i = soma_i + numero
    return qtd_p, qtd_i, soma_p, soma_i
try:
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um numero: "))
    n3 = float(input("Digite um numero: "))
    n4 = float(input("Digite um numero: "))
    lista = [n1, n2, n3, n4]
    resultado = analisar_lista(lista)
    print(resultado)
except:
    print("Valores inválidos")