#pratica 218
def classificar_compra(valor):
    if valor >= 100:
        return("Compra aprovada")
    else:
        return("Compra não aprovada")
try:
    compra = float(input("Qual o valor da compra: "))
    resultado = classificar_compra(compra)
    print(resultado)
except:
    print("Valor inválido")