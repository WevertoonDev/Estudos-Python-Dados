#pratica 211
def calcular_media(media):
    soma = 0
    for numero in media:
        soma = soma + numero
    media = soma / len(media)
    return media
def classificar_media(media):
    media = calcular_media(media)
    if media >= 7:
        return("Aprovado")
    elif media >= 5:
        return("Recuperação")
    else:
        return("Reprovado")
nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))
lista = [ nota1, nota2, nota3]
resultado = classificar_media(lista)
print(resultado)