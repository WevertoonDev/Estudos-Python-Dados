#pratica 104 input() + or
nome = input("Digite seu nome: ")
cinema = input("Qual dia vc quer ir no cinema? ")
if cinema == "sabado" or cinema == "domingo":
    print("Olá,", nome,"Você tem direito à promoção")
else:
    print("Olá,",nome,"A promoção não é válida nesse dia.")