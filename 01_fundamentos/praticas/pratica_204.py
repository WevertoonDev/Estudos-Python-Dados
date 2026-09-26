#pratica_204
def classificar_nota(nota):
    if nota >= 7:
        return("Aprovado")
    elif nota >= 5:
        return("Recuperação")
    else:
        return("Reprovado")
aluno = float(input("Digite sua nota: "))
resultado = classificar_nota(aluno)
print(resultado)