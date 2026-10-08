#pratica 278
def contar_numeros(numeros):
    qtd_p = 0
    qtd_n = 0
    qtd_z = 0
    for numero in numeros:
        if numero > 0:
            qtd_p = qtd_p + 1
        elif numero < 0:
            qtd_n = qtd_n + 1
        else:
            qtd_z = qtd_z + 1
    resultado = {"Positivos": qtd_p,
                 "Negativos": qtd_n,
                 "Zero": qtd_z}
    return resultado
numero = [ 5, -2, 0, 8, -3, 0]
resultado = contar_numeros(numero)
print(resultado)