#pratica 228
def classificar_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return("Aprovado")
    elif media >= 5:
        return("Recuperação")
    else:
        return("Reprovado")
try:
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite sua nota: "))
    nota3 = float(input("Digite sua nota: "))
    resultado = classificar_media(nota1, nota2, nota3)
    print(resultado)
except:
    print("Notas inválidas")