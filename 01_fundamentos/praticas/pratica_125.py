#pratica 125 input + condicoes 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))
if idade >= 18 and nota >= 7:
    print("Adulto aprovado")
elif idade >= 18 and nota < 7:
    print("Adulto em recuperação")
elif idade < 18 and nota >= 7:
    print("Menor aprovado")
else:
    print("Menor em recuperação")