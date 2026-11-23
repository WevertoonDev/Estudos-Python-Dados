ano = []
dia = int(input("Digite o Dia: "))
mes = int(input("Digite o Mês: "))
ano = int(input("Digite o Ano: "))
if (ano % 4 == 0) or (ano % 400 == 0 and ano % 100 != 0):
    print(f"O ano {ano}, é bissexto")
