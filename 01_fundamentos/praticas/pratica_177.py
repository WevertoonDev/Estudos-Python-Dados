#pratica 177 funções trabalhando juntas
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2 
def classificar_aluno(nota1, nota2):
    media = calcular_media(nota1, nota2)
    if media >= 7:
        return("Aprovado")
    elif media >= 5:
        return("Recuperação")
    else:
        return("Reprovado")
resultado = classificar_aluno(8, 6)
print(resultado)