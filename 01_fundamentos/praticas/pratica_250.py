#pratica 250
def analisar_lista(numeros):
    qtd = 0
    soma = 0
    maior = None
    menor = None
    for numero in numeros:
        qtd = qtd + 1
        soma = soma + numero
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
    if qtd == 0:
        return 0, 0, maior, menor
    return qtd, soma, maior, menor
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