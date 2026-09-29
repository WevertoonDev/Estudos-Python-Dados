#pratica 234
def contar_maiores(numeros):
    qtd = 0
    for numero in numeros:
        if numero > 10:
            qtd = qtd + 1
    return qtd
try:
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um numero: "))
    n3 = float(input("Digite um numero: "))
    n4 = float(input("Digite um numero: "))
    lista = [n1, n2, n3, n4]
    qtd = contar_maiores(lista)
    print(qtd)
except:
    print("Valores inválidos")