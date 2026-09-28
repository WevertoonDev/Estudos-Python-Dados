#Pratica 217
def calcular_dobro(numero):
    return numero * 2
try:
    nu = float(input("Digite um numero: "))
    resultado = calcular_dobro(nu)
    print(resultado)
except:
    print("Valor inválido")