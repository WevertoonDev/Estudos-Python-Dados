#pratica 214
def calcular_dobro(numero):
    return numero * 2
try:
    numero = float(input("Digite um numero: "))
    resultado = calcular_dobro(numero)
    print(resultado)
except:
    print("Valor inválido")