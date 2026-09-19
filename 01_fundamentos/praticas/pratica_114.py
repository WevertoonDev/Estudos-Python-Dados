#Pratica_114_Classificação_de_Idade
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")