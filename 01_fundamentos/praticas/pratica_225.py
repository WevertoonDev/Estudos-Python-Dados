#pratica 225
def calcular_desconto(valor):
    if valor >= 200:
        desconto = valor * 0.10
        valor_final = valor - desconto
        return valor_final
    else:
        return valor
try:
    compra = float(input("Qual foi o valor da compra: "))
    resultado = calcular_desconto(compra)
    print(resultado)
except:
    print("Valor inválido")