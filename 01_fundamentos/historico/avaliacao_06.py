dia = int(input("Digite o Dia: "))
mes = int(input("Digite o Mês: "))
ano = int(input("Digite o Ano: "))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    bissexto = True
else:
    bissexto = False
if dia < 1 or dia > 31 and mes < 1 or mes > 12:
    print("Data inválida")
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("Esse mês tem 31 dias")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Esse mês tem 30 dias")
if mes == 2 and bissexto == True and dia > 29:
    print("Data inválida")
elif mes == 2 and bissexto == False and dia > 28:
    print("Data inválida")
if mes < 1 or mes > 12:
    print("Mês invalido")
if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    print("Data inválida")