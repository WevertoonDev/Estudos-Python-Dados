#pratica 119 condicoes com parenteses
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
ingresso = input("Você possui ingresso? ")
if ingresso == "sim" and (idade >= 18 or estudante == "sim"):
    print("Você pode entrar.")
else:
    print("Você não pode entrar.")