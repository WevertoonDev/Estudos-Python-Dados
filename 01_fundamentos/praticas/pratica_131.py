#pratica 131 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Qual é sua renda mensal: "))
estudante = input("Você é estudante? ")
if idade >= 18 and salario <= 2000 and estudante == "sim":
    print("Benefício completo")
elif idade >= 18 and salario <= 3000:
    print("Benefício parcial")
elif idade < 18 and estudante == "sim" and salario <= 2000:
    print("Benefício estudantil")
else:
    print("Sem benefício")