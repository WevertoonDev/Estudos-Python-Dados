#Pratica_110_Desconto_por_Idade_e_Valor
idade = int(input("Digite sua idade: "))
valor = float(input("Qual o valor da compra: "))
if idade >= 18 and valor >= 100 or idade < 18:
    print("Você tem direito ao desconto.")
else:
    print("Você não tem direito ao desconto")