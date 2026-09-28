#pratica 219
def calcular_media(nota1, nota2):
    return (nota1 + nota2)/ 2
try:
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite sua nota: "))
    resultado = calcular_media(nota1, nota2)
    print(resultado)
except:
    print("Notas inválidas")