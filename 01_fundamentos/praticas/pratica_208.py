#pratica 208
def calcular_dobro(numero):
    return numero * 2
def calcular_dobro_mais_dez(numero):
    resultado = calcular_dobro(numero)
    return resultado + 10
digito = int(input("Digite um numero: "))
resultado = calcular_dobro_mais_dez(digito)
print(resultado)