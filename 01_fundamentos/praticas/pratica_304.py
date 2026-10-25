#pratica 304
vendas = [100, 200, 250, 300]
qtd = 0
soma = 0
for numero in vendas:
    if numero > 500:
        qtd += 1
        soma += numero
if qtd > 0:
    media = soma /qtd
    print(f"A média é R$ {media:.2f}")
else:
    print("Nenhuma venda acima de R$ 500")
print(f"A soma é {soma} e a quantidade {qtd}")