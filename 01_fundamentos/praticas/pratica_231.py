#pratica 231 avaliação
def analisar_compra(idade, estudante, valor):
    if idade >= 18 and estudante == "sim" and valor >= 200:
        return("Desconto especial")
    elif idade >= 18 and valor >= 200:
        return("Desconto normal")
    elif idade >= 18 and estudante == "sim":
        return("Desconto estudante")
    else:
        return("Sem desconto")
try:
    idade = int(input("Digite sua idade: "))
    estudante = input("Você é estudante? ")
    valor = float(input("Qual foi o valor da compra: "))
    resultado = analisar_compra(idade, estudante, valor)
    print(resultado)
except:
    print("Dados inválidos")