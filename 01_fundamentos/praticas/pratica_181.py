#pratica 181 funcoes trbalhando com lista
def calcular_soma(lista):
    soma = 0
    for numero in lista:
        soma = soma + numero
    return soma 
def classificar_soma(lista):
    resultado = calcular_soma(lista)
    if resultado >= 50:
        return("Soma alta")
    else:
        return("Soma baixa")
resultado = classificar_soma(lista=[10, 20, 30])
print(resultado)