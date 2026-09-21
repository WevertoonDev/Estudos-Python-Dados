#Pratica_126_Input_+_Condições
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite sua renda mensal: "))
estudante = input("Você é estudante? ")
if idade >= 18 and salario <= 2000 and estudante == "sim":
    print("Benefício completo")
elif idade >= 18 and salario <= 3000:
    print("Benefício parcial")
elif idade < 18 and estudante == "sim":
    print("Benefício estudantil")
else:
    print("Sem benefício")