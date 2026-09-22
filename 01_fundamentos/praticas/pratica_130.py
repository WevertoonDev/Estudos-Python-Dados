#Pratica_130_Desconto_de_Ingresso
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
valor = float(input("Valor do ingresso: "))
if idade < 12:
    print("Entrada gratuita")
elif idade >= 12 and idade <= 17 and estudante == "sim" or (idade >= 18 and estudante == "sim"):
    print("Meia entrada")
elif idade >= 18 and valor >= 100:
    print("Desconto de 10 %")
else:
    print("Preço normal")
