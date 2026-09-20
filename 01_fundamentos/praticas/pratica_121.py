#pratica 121 condiçoes compostas
idade = int(input("Digite sua idade: "))
renda = float(input("Qual é sua renda? "))
estudante = input("Você é estudante? ")
if idade >= 18 and renda <= 3000 and (estudante == "sim" or renda < 1500):
    print("Você tem direito ao benefício.")
else:
    print("Você não tem direito ao benefício.")