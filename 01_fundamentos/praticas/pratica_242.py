#pratica 242
def analisar_numeros(numeros):
    qtd = 0
    soma = 0
    maior = None
    menor = None
    for numero in numeros:
        if numero > 10:
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
        return 0, 0, 0, 0, 0
    media = soma / qtd
    return qtd, soma, media, maior, menor
try:
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um numero: "))
    n3 = float(input("Digite um numero: "))
    n4 = float(input("Digite um numero: "))
    lista = [n1, n2, n3, n4]
    resultado = analisar_numeros(lista)
    print(resultado)
except:
    print("Valores inválidos")