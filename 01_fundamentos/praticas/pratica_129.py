#pratica 129 desconto por faixa etária
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
valor = float(input("Qual foi o valor? "))
estudante = input("Você é estudante? ")
if idade >= 18 and estudante == "sim" and valor >= 200:
    print("Desconto de 20%")
elif idade >= 18 and valor >= 200:
    print("Desconto de 10%")
elif idade < 18 and estudante == "sim":
    print("Desconto de 5%")
else:
    print("Sem desconto")