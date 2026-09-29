#pratica 233
def calcular_soma(numeros):
    soma = 0
    for numero in numeros:
        soma = soma + numero
    return soma
try:
    n1 = float(input("Digite a nota da turma: "))
    n2 = float(input("Digite a nota da turma: "))
    n3 = float(input("Digite a nota da turma: "))
    lista = [n1, n2, n3]
    soma = calcular_soma(lista)
    print(soma)
except:
    print("Valores inválidos")