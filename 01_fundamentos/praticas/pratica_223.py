#pratica 223
def avaliar_aluno(nota1, nota2):
    media =(nota1 + nota2)/2
    if media >= 7:
        return("Aprovado")
    elif media >= 5:
        return("Recuperação")
    else:
        return("Reprovado")
try:
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite sua nota: "))
    media = avaliar_aluno(nota1, nota2)
    print(media)
except:
    print("Notas inválidas")