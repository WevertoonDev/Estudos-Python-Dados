#pratica 227
def verificar_desconto(idade, valor):
    if idade >= 18 and valor >= 200:
        return("Desconto aprovado")
    else:
        return("Sem desconto")
try:
    idade = int(input("Digite sua idade: "))
    valor = float(input("Digite o valor da comprar: "))
    resultado = verificar_desconto(idade, valor)
    print(resultado)
except:
    print("Dados inválidos")