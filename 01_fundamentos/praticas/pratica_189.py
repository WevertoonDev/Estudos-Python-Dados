#pratica 189
def analisar_notas(lista):
    maior = None
    soma = 0
    for numero in lista:
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        soma = soma + numero
    media = soma / len(lista)
    return maior
def classificar_maior_nota(lista):
    maior = analisar_notas(lista)
    if maior >= 9:
        return("Excelente")
    elif maior >= 7:
        return("Bom")
    else:
        return("Precisa melhorar")
resultado = classificar_maior_nota(lista=[6, 8, 7, 9])
print(resultado)