#pratica 111 entrada mais condicoes
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
valor = float(input("Qual é o  valor da compra: "))
if idade >= 18 and estudante == "sim" or valor >= 200:
    print("Você tem direito ao desconto")
else:
    print("Você não tem direito ao desconto")