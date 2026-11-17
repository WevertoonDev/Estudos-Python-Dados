dia = int(input("Digite o Dia: "))
mes = int(input("Digite o Mês: "))
ano = int(input("Digite o Ano: "))
if dia < 1 or dia > 32:
    print("Dia invalido")
elif mes < 1 or mes > 12:
    print("Mês invalido")
print(f"Hoje é {dia}/{mes}/{ano}")
