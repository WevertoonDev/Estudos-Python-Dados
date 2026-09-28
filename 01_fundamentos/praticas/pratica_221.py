#pratica 221
def verificar_compra(idade, valor):
    if idade >= 18 and valor >= 200:
        return("Compra aprovada")
    else:
        return("Compra não aprovada")
try:
    idade = int(input("Digite sua idade: "))
    compra = float(input("Qual o valor da compra: "))
    resultado = verificar_compra(idade, compra)
    print(resultado)
except:
    print("Dados inválidos")