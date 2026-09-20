#pratica 123 operadores de comparacao
idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))
if idade < 18:
    print("Menor de idade")
elif idade >= 18:
    print("Maior de idade")
if nota >= 7:
    print("Aprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
else:
    print("Reprovado")