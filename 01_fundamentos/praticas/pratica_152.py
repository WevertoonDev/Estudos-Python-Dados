#Pratica_152
def calcular_desconto(valor):
    if valor >= 200:
        return valor * 0.90
    else:
        return valor
resultado = calcular_desconto(300)
print(resultado)