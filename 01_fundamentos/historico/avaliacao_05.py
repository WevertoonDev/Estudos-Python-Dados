numero = int(input("Digite um numero: "))
lista_primos = []
for numeros in range(2, numero + 1):
    contador = 0
    for divisor in range(1, numeros + 1):
        resto = numeros % divisor
        if resto == 0:
            contador += 1
    if contador == 2:
        lista_primos.append(numeros)
print(lista_primos)