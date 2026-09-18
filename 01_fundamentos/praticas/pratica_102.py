#pratica input() + if + and
idade = int(input("Digite sua idade: "))
carteira = input("Possui carteira? ")
if idade >= 18 and carteira == "sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir.")