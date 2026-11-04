vendas = [200, 250, 300, 400]
for i in range(1,len(vendas)):
    diferenca = vendas[i] - vendas[i - 1]
    print(f"Diferença: {diferenca}")