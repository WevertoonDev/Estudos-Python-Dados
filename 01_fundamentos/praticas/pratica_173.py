#pratica 173
def calcular_dobro(numero):
    return numero * 2
def verificar_dobro(numero):
    resultado = calcular_dobro(numero)
    if resultado >= 20:
        return ("Valor alto")
    else:
        return("Valor baixo")
resultado = verificar_dobro(10)
print(resultado)