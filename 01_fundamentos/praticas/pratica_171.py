#pratica 171 funcoes
def calcular_triplo(numero):
    return numero * 3
def triplo_mais_dez(numero):
    resultado = calcular_triplo(numero)
    return resultado + 10
resultado = triplo_mais_dez(10)
print(resultado)