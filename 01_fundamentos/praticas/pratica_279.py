#pratica 278
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
def analisar_numeros(numeros):
    qtd = 0
    qtd_i = 0
    for numero in numeros:
        par = eh_par(numero)
        qtd = qtd + par
        qtd_i = qtd_i + (not par)
    resulatdo = {"Pares": qtd,
                 "Impares": qtd_i}
    return resulatdo
numeros =[2, 7, 4, 9, 10]
resultado = analisar_numeros(numeros)
print(resultado)