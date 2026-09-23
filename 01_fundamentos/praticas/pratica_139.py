nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Qual é sua renda: "))
estudante = input("Você é estudante? ")
valor = float(input("Qual é o valor da compra: "))
if idade >= 18 and estudante == "sim" and renda <= 2500 and valor >= 300:
    print("Benefício completo")
elif idade >= 18 and renda <= 4000 and valor >= 200:
    print("Benefício parcial")
elif idade < 18 and estudante == "sim" and valor >= 100:
    print("Benefício estudantil")
else:
    print("Sem benefício")