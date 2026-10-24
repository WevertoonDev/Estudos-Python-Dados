#pratica 303
vendas = [150, 400, 250, 700, 100, 600]
soma = 0
qtd = 0
for valor in vendas:
    if valor > 300:
        soma += valor
        qtd += 1
media = soma / qtd
print(f"A média é {media:.2f}")