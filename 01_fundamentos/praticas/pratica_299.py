vendas = [200, 350, 150, 500, 700, 100]
soma = 0
for valor in vendas:
    if valor > 300:
        soma = soma + valor
print(f"O total da soma é: {soma}")