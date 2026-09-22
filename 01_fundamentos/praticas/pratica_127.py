#pratica 127 classificaçao de compra
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
valor = float(input("Qual foi o valor da comprar: "))
if idade >= 18 and valor >= 200:
    print("Compra com desconto")
elif idade >= 18 and valor < 200:
    print("Compra normal")
elif idade < 18:
    print("Compra não permitida")