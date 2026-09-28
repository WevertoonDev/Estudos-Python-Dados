#pratica 229
def analisar_numeros(numero1, numero2):
    soma = numero1 + numero2
    if soma >= 100:
        return("Soma alta")
    elif soma >= 50:
        return("Soma média")
    else:
        return("Soma baixa")
try:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um numero: "))
    soma = analisar_numeros(numero1, numero2)
    print(soma)
except:
    print("Valores inválidos")