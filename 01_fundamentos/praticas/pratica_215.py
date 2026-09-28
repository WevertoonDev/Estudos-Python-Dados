def classificar_compra(valor):
    if valor >= 200:
        return("Compra grande")
    elif valor >= 100:
        return("Compra média")
    else:
        return("Compra pequena")
try:
    compra = float(input("Qual é valor da compra: "))
    resultado = classificar_compra(compra)
    print(resultado)
except:
    print("Valor inválido")