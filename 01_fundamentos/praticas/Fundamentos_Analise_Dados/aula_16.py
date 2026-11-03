#aula 16
vendas = [100, 150, 200]

for i in range(1, len(vendas)):
    diferenca = vendas[i] - vendas[i - 1]
    print(f"Diferença: {diferenca}")