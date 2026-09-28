#pratica 220
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2
try:
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite sua nota: "))
    media = calcular_media(nota1, nota2)
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
except:
    print("Notas inválidas")