#pratica 109 input() + condicoes
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
if idade >= 18 and estudante == "sim" or idade < 18:
    print("Você tem direito ao desconto.")
else:
    print("Você não tem direito ao desconto.")