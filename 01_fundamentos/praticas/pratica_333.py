#pratica_333
vendas = [150, 300, 250, 400, 100]
qtd = 0
for venda in vendas:
    if venda > 200:
        qtd += 1
print(f"A quantidade de vendas maior que 200 é {qtd}")