#Pratica_120_Condições _+_Parênteses
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
carteira = input("Você possui carteira de habilitaçaõ? ")
if idade >= 18 and (estudante == "sim" or carteira == "sim"):
    print("Você pode participar.")
else:
    print("Você não pode participar.")