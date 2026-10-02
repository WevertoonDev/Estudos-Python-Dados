#pratica 252 
def analisar_lista(numeros):
    qtd = 0
    qtd_b = 0
    qtd_i = 0
    maior = None
    for numero in numeros:
        if numero > 0:
            qtd = qtd + 1
        if numero < 0:
            qtd_b = qtd_b + 1
        if numero == 0:
            qtd_i = qtd_i + 1
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
    return qtd, qtd_b, qtd_i, maior
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