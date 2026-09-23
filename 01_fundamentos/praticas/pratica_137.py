#pratica 137 classificaçao de aluno 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
nota = float(input("Digite sua nota: "))
if idade >= 18 and nota >= 9 and estudante == "sim":
    print("Excelente com benefício")
elif idade >= 18 and nota >= 9:
    print("Aprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
elif nota < 5:
    print("Reprovado")
else:
    print("Sem classificação")