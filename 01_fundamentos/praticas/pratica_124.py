#pratica 124 faixas de valores
nota = float(input("Digite sua nota: "))
if nota >= 9 and nota <= 10:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")