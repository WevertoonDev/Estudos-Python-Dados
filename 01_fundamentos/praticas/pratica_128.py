#pratica 128 desconto por idade e valor
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
valor = float(input("Qual foi o valor? "))
estudante = input("Você é estudante? ")
if idade >= 18 and estudante == "sim" and valor >= 150:
    print("Desconto especial")
elif idade >= 18 and valor >= 150:
    print("Desconto normal")
elif idade < 18 and estudante == "sim" :
    print("Desconto estudantil")
else:
    print("Sem desconto")
