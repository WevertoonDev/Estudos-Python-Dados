#Pratica_112_Input_+_And_+_Or
idade = int(input("Digite sua idade: "))
ingresso = input("Qual é o tipo do seu ingresso? ")
valor = float(input("Qual o valor da compra? "))
if idade < 12 or idade >= 18 and ingresso == "vip":
    print("Você tem entrada gratuita.")
else:
    print("Você precisa pagar a entrada.")