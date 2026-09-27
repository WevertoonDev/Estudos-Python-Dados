#pratica 210
def calcular_maior_salario(salario):
    maior = None
    for numero in salario:
        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
    return maior
def classifique_maior_salario(salario):
    maior = calcular_maior_salario(salario)
    if maior >= 5000:
        return("Salário alto")
    elif maior >= 3000:
        return("Salário médio")
    else:
        return("Salário baixo")
salario1 = float(input("Qual é o seu salario: "))
salario2 = float(input("Qual é o seu salario: "))
salario3 = float(input("Qual é o seu salario: "))
lista = [salario1, salario2, salario3]
resultado = classifique_maior_salario(lista)
print(resultado)