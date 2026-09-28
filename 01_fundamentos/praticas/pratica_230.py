#pratica 230
def analisar_aluno(idade, nota1, nota2):
    media = (nota1 + nota2)/2
    if idade >= 18 and media >= 7:
        return("Adulto aprovado")
    elif idade >= 18 and media < 7:
        return("Adulto reprovado")
    elif idade < 18 and media >= 7:
        return("Menor aprovado")
    else:
        return("Menor reprovado")
try:
    idade = int(input("Digite sua idade: "))
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite sua nota: "))
    media = analisar_aluno(idade, nota1, nota2)
    print(media)
except:
    print("Dados inválidos")