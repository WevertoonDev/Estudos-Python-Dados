#pratica 209 
def calcular_total(total):
    soma = 0
    for numero in total:
        soma = soma + numero
    return soma
def calcular_media(total):
    soma = calcular_total(total)
    media = soma / len(total)
    return media
compra1 = float(input("Qual o valor da compra: "))
compra2 = float(input("Qual o valor da compra: "))
compra3 = float(input("Qual o valor da compra: "))
lista = [compra1, compra2, compra3]
media = calcular_media(lista)
total = calcular_total(lista)
print("Total:", total,"Média:",media)