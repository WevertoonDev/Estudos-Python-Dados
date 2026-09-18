#pratica 103 consolidadndo input() + and
idade = int(input("Digite sua idade: "))
ingresso = input("Possui ingresso? ")
if idade >= 18 and ingresso == "sim":
    print("Entrada permitida")
else:
    print("Entrada não permitida")