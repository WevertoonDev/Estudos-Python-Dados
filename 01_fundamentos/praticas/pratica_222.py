#pratica 222
def classificar_aluno(nota, idade):
    if idade >= 18 and nota >=7:
        return("Adulto aprovado")
    elif idade >= 18 and nota <7:
        return("Adulto reprovado")
    elif idade < 18 and nota >= 7:
        return("Menor aprovado")
    else:
        return("Menor reprovado")
try:
    idade = int(input("Digite sua idade: "))
    nota = float(input("Digite sua nota: "))
    resultado = classificar_aluno(nota, idade)
    print(resultado)
except:
    print("Dados inválidos")