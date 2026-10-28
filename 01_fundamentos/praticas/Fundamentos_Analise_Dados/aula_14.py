#aula 14
vendas = [100, 300, 500, 700, 900, 1100]
qtd = len(vendas)
indice1 = qtd // 2 - 1
indice2 = qtd // 2
mediana = (vendas[indice1] + vendas[indice2]) / 2
print(mediana)