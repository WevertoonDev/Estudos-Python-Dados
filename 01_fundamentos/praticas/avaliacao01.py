caixa = 5000
vendas = 3200
despesas = 1150
faturamento = vendas
novo_faturamento = faturamento - despesas
saldo_final = novo_faturamento + caixa
print(f"O faturamento foi R$ {faturamento:.2f}, saldo depois das despesas foi de R$ {novo_faturamento:.2f} saldo final é de R$ {saldo_final:.2f}")