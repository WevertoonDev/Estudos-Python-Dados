#pratica 232
def analisar_notas(notas):
    media = (notas[0] + notas[1] + notas[2]) / 3
    if media >=7:
        return("Turma aprovada")
    elif media >= 5:
        return("Turma em recuperação")
    else:
        return("Turma reprovada")
try:
    n1 = float(input("Digite a nota da turma: "))
    n2 = float(input("Digite a nota da turma: "))
    n3 = float(input("Digite a nota da turma: "))
    lista = [n1, n2, n3]
    resultado = analisar_notas(lista)
    print(resultado)
except:
    print("Notas inválidas")
