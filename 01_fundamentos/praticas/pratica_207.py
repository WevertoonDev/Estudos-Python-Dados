#pratica 207 input+funçoes+lsta+calculo
def calcular_total(precos):
    soma = 0
    for numero in precos:
        soma = soma + numero
    return soma
produto1 = float(input("Qual o preco: "))
produto2 = float(input("Qual o preco: "))
produto3 = float(input("Qual o preco: "))
lista = [produto1, produto2, produto3]
resultado = calcular_total(lista)
print(resultado)