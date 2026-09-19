#pratica 113 consolidando input + condiçoes
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
if idade < 12:
    print("Entrada gratuita")
elif idade >= 12 and estudante == "sim":
    print("Meia entrada")
else:
    print("Entrada inteira")