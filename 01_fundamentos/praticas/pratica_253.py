#pratica 253
def analisar_lista(numeros):
    qtd_p = 0
    qtd_i = 0
    maior = None
    menor = None
    for numero in numeros:
        if numero % 2 == 0:
            qtd_p = qtd_p + 1
        else:
            qtd_i = qtd_i + 1
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
    return qtd_p, qtd_i, maior, menor
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