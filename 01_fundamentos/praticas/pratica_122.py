#Pratica_122_Vamos_Subir_Mais_1_Degrau
idade = int(input("Digite sua idade: "))
renda = float(input("Qual é sua renda: "))
estudante = input("Você é estudante? ")
if idade >= 18 and renda <= 3000 or (idade < 18 and estudante == "sim" and renda <= 2000):
    print("Tem direito.")
else:
    print("Não tem direito.")