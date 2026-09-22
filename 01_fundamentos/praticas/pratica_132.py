#Pratica_132_Benefício_por_Idade_Renda_e_Estudante
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Qual é sua renda mensal: "))
estudante = input("Você é estudante? ")
if idade >= 18 and salario <= 2500 and estudante == "sim":
    print("Benefício completo")
elif idade >= 18 and salario <= 2500:
    print("Benefício parcial")
elif idade < 18 and estudante == "sim":
    print("Benefício estudantil")
else:
    print("Sem benefício")