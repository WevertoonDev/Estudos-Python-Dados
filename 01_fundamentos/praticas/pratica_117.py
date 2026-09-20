#pratica 117 condicoes mais not
idade = int(input("Digite sua idade: "))
habilitacao = input("Você possui habilitação? ")
carro = input("O carro está disponivel? ")
if idade >= 18 and habilitacao == "sim" and not carro == "sim":
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")