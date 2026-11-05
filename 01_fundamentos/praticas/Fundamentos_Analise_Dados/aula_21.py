#aula 21
vendas = [100, 150, 180, 300]

maior_salto = vendas[1] - vendas[0]
venda_anterior = vendas[0]
venda_atual = vendas[1]

for i in range(2, len(vendas)):
    diferenca = vendas[i] - vendas[i - 1]

    if diferenca > maior_salto:
        maior_salto = diferenca
        venda_anterior = vendas[i - 1]
        venda_atual = vendas[i]

print(f"Maior salto: {maior_salto}")
print(f"Venda anterior: {venda_anterior}")
print(f"Venda atual: {venda_atual}")