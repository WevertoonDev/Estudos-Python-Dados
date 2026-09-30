#pratica 237
def analisar_maiores(numeros):
    soma = 0
    qtd = 0
    for numero in numeros:
        if numero > 10:
            qtd = qtd  + 1
            soma = soma + numero
    if qtd == 0:
        return 0, 0
    media = soma / qtd
    return qtd, media
try:
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um numero: "))
    n3 = float(input("Digite um numero: "))
    n4 = float(input("Digite um numero: "))
    lista = [n1, n2, n3, n4]
    resultado = analisar_maiores(lista)
    print(resultado)
except:
    print("Valores inválidos")