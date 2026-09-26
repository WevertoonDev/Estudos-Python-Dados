#Pratica_180_Funções_Trabalhando_Juntas
def calcular_dobro(numero):
    return numero * 2
def analisar_numero(numero):
    resultado = calcular_dobro(numero)
    if resultado > 20:
        return("Maior")
    elif resultado == 20:
        return("Igual")
    else:
        return("Menor")
resultado = analisar_numero(10)
print(resultado)