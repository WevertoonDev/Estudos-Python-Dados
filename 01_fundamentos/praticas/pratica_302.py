#pratica 302
vendas = [150, 400, 250, 700, 100, 600]
soma = 0
qtd = 0
for valor in vendas:
    if valor > 300:
        soma += valor
        qtd += 1
print(f"A soma é {soma} e a quantidade é {qtd}")