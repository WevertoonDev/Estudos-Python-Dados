#pratica 138 situaçao difierente
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
habilitacao = input("Você tem carteira de motorista? ")
carro = input("Você possui carro? ")
if idade >= 18 and habilitacao == "sim" and carro == "sim":
    print("Pode dirigir")
elif idade >= 18 and habilitacao == "sim":
    print("Tem habilitação, mas não tem carro")
elif idade >= 18:
    print("Precisa tirar a carteira")
else:
    print("Ainda não pode dirigir")