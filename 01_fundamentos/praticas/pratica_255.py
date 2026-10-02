#pratica 255
def analisar_lista(numeros):
    qtd_p = 0
    qtd_n = 0
    qtd_z = 0
    soma = 0
    menor = None
    for numero in numeros:
        soma = soma + numero
        if numero > 0:
            qtd_p = qtd_p + 1
        if numero < 0:
            qtd_n = qtd_n + 1
        if numero == 0:
            qtd_z = qtd_z + 1
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
    return qtd_p, qtd_n, qtd_z, soma, menor
try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    n4 = int(input("Digite um numero: "))
    lista = [n1, n2, n3, n4]
    resultado = analisar_lista(lista)
    print(resultado)
except:
    print("Valores inválidos")