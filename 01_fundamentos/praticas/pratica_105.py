#Pratica_105_Input()_+_and_+_or
idade = int(input("Digite sua idade: "))
ingresso = input("Possui ingresso? ")
responsavel = input("Esta acompanhado do responsével? ")
if idade >= 18 and ingresso == "sim" or idade < 18 and responsavel == "sim":
    print("Pode entrar")
else:
    print("Não pode entrar")