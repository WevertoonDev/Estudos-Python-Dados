#pratica 248
def analisar_lista(numeros):
    qtd = 0
    qtd_n = 0
    qtd_z = 0
    soma = 0
    qtd_total = 0
    for numero in numeros:
        qtd_total = qtd_total +1
        soma = soma + numero
        if numero > 0:
            qtd = qtd + 1
        if numero < 0:
            qtd_n = qtd_n + 1
        if numero == 0:
            qtd_z = qtd_z + 1
    if qtd_total == 0:
        return 0, 0, 0, 0
    return qtd, qtd_n, qtd_z, soma
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