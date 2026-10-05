#pratica 267 ultima
def analisar_lista(numeros):
    qtd_p = 0
    qtd_n = 0
    soma_p = 0
    maior_i = None
    media = None
    soma_t = 0
    qtd_t = 0
    for numero in numeros:
        qtd_t = qtd_t + 1
        soma_t = soma_t + numero
        if numero > 0:
            qtd_p = qtd_p + 1
        if numero < 0:
            qtd_n = qtd_n + 1
        if numero % 2 == 0:
            soma_p = soma_p + numero
        else:
            if maior_i is None:
                maior_i = numero
            elif numero > maior_i:
                maior_i = numero
    if qtd_t > 0:
        media = soma_t / qtd_t
    else:
        media = None
    return qtd_p, qtd_n, soma_p, maior_i, media
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    n5 = int(input("Digite um numero: "))
    n6 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4, n5, n6]
    resultado = analisar_lista(lista)
    print(resultado)
except ValueError:
    print("Valores inválidos")