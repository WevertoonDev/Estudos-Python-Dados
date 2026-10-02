#pratica 247
def analisar_lista(numeros):
    qtd = 0
    soma = 0
    qtd_m = 0
    for numero in numeros:
        qtd = qtd + 1
        soma = soma + numero
        if numero > 0:
            qtd_m = qtd_m + 1
    if qtd == 0:
        return 0, 0, 0, 0
    media = soma / qtd
    return qtd, soma, media, qtd_m
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