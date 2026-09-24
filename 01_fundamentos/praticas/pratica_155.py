#pratica 155
def calcular_resultado(nota):
    if nota >= 7:
        return("Aprovado")
    elif nota >= 5:
        return("Recuperação")
    else:
        return("Reprovado")
resultado = calcular_resultado(nota = 6)
print(resultado)