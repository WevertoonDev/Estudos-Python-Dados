#Pratica_116_Condições_Compostas
idade = int(input("Digite sua idade: "))
renda = float(input("Qual é sua renda mensal? "))
estudante = input("Você é estudande? ")
if idade >= 18 and renda < 3000 or estudante == "sim" and renda < 2000:
    print("Você tem direito ao benefício.")
else:
    print("Você não tem direito ao benefício.")