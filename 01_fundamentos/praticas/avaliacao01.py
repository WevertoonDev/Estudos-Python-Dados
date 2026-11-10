vendas = [100, 250, 100, 400, 150, 250, 500, 100]
qtd = 0
qtd_m = 0
soma = 0
indice = 0
while indice < len(vendas):
    if vendas[indice] == 100:
        qtd += 1
    if vendas[indice] >= 250:
        qtd_m += 1
        soma += vendas[indice]
    indice += 1
print(qtd, qtd_m, soma)