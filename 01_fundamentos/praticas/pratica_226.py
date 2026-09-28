#pratica 226
def verificar_numero(numero):
    if numero >= 0:
        return("Número positivo ou zero")
    else:
        return("Número negativo")
try:
    usuario = float(input("Digite um numero: "))
    resultado = verificar_numero(usuario)
    print(resultado)
except:
    print("Número inválido")