#pratica 205
def calcular_media(notas):
    soma = 0
    for numero in notas:
        soma = soma + numero
    media = soma / len(notas)
    return media
aluno1 = float(input("Digite sua primeira nota: "))
aluno2 = float(input("Digite sua segunda nota: "))
aluno3 = float(input("Digite sua terceira nota: "))
lista = [aluno1, aluno2, aluno3]
resultado = calcular_media(lista)
print(resultado)