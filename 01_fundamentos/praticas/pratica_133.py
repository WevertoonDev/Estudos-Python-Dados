#pratica 133 benefício por idade, renda e estudante
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Qual é sua renda mensal: "))
estudante = input("Você é estudante? ")
compra = float(input("Qual é o valor da comprar: "))
if idade >= 18 and estudante == "sim" and salario <= 2000 and compra >= 200:
    print("Benefício completo")
elif idade >= 18 and salario <= 3000 and compra >= 200:
    print("Benefício parcial")
elif idade < 18 and estudante == "sim" and compra >= 100:
    print("Benefício estudantil")
else:
    print("Sem benefício")