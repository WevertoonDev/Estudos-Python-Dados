#pratica 260 analise completta de uma lista
def analisar_lista(numeros):
    qtd_p = 0
    qtd_n = 0
    qtd_z = 0
    soma = 0
    maior = None
    for numero in numeros:
        if numero > 0:
            qtd_p = qtd_p + 1
            if maior is None:
                maior = numero
            elif numero > maior:
                maior = numero
        elif numero < 0:
            qtd_n = qtd_n + 1
            soma = soma + numero
        else:
            qtd_z = qtd_z + 1
    return qtd_p, qtd_n, qtd_z, soma, maior
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