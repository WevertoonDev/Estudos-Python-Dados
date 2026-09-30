#pratica 235
def somar_maiores(numeros):
    soma = 0
    for numero in numeros:
        if numero > 10:
            soma = soma + numero
    return soma
try:
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um numero: "))
    n3 = float(input("Digite um numero: "))
    n4 = float(input("Digite um numero: "))
    lista = [n1, n2, n3, n4]
    soma = somar_maiores(lista)
    print(soma)
except:
    print("valores inválidos ")