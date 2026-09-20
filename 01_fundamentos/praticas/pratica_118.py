#Pratica_118_and_+_OR
idade = int(input("Digite sua idade: "))
ferias = input("Você está de férias? ")
viagem = input("Você tem passagem? ")
if viagem == "sim" and (idade >= 18 or ferias == "sim"):
    print("Você pode viajar.")
else:
    print("Você não pode viajar.")
    