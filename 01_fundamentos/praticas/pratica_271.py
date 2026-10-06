#pratica 271 funcoes e organizaçao de codigo
def calcular_estatisticas(lista):
    qtd_p = 0
    qtd_n = 0
    soma = 0
    qtd_t = 0
    for numero in lista:
        soma = soma + numero
        qtd_t = qtd_t + 1
        if numero > 0:
            qtd_p = qtd_p + 1
        if numero < 0:
            qtd_n = qtd_n + 1
    if qtd_t > 0:
        media = soma / qtd_t
    else:
        media = None
    return qtd_p, qtd_n, soma, media
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5]
    resultado = calcular_estatisticas(lista)
    print(resultado)
except ValueError:
    print("Valores inválidos")