#pratica 115 classificacao mais estudante
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? ")
if idade < 12:
    print("Entrada gratuita")
elif idade >= 12 and idade <= 17:
    print("Meia entrada")
elif idade <= 59 and estudante == "sim":
    print("Meia entrada")
elif idade <= 59 and estudante == "não":
    print("Entrada inteira")
else:
    print("Meia entrada")