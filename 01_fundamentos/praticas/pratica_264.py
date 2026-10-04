#pratica 264 avaliacao final
def analisar_lista(numeros):
    qtd = 0
    qtd_m = 0
    soma = 0
    qtd_n = 0
    media = None
    qtd_t = 0
    soma_t = 0
    for numero in numeros:
        qtd_t = qtd_t + 1
        soma_t = soma_t + numero
        if numero > 10:
            qtd = qtd + 1
        if numero <= 10:
            qtd_m = qtd_m + 1
        if numero > 0:
            soma = soma + numero
        if numero < 0:
            qtd_n = qtd_n + 1
    if qtd_t > 0:
        media = soma_t / qtd_t
    else:
        media = None
    return qtd, qtd_m, soma, qtd_n, media
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