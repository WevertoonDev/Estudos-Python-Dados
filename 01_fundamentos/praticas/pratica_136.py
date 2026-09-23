#Pratica_135_Sistema_de_Aprovação
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
nota = float(input("Digite sua nota: "))
if idade >= 18 and nota >= 7 and estudante == "sim":
    print("Aprovado com benefício")
elif idade >= 18 and nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")