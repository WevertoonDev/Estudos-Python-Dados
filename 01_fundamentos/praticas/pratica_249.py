#pratica 249
def analisar_lista(numeros):
    qtd = 0
    qtd_b = 0
    qtd_i = 0
    soma = 0
    qtd_t = 0
    for numero in numeros:
        qtd_t = qtd_t + 1
        soma = soma + numero
        if numero > 10:
            qtd = qtd + 1
        if numero < 10:
            qtd_b = qtd_b + 1
        if numero == 10:
            qtd_i = qtd_i + 1
    if qtd_t == 0:
        return 0, 0, 0, 0, 0
    return qtd, qtd_b, qtd_i, soma, qtd_t
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