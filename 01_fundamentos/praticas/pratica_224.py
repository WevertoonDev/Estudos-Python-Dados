#pratica 224
def analisar_compra(valor):
    if valor >= 200:
        return valor * 0.50
    else:
        return valor
try:
    compra = float(input("Qual o valor da compra: "))
    resulatdo = analisar_compra(compra)
    print(resulatdo)
except:
    print("Valor inválido")