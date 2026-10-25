#pratica 306
def analisar_vendas(vendas):
    qtd = 0
    soma = 0
    for venda in vendas:
        if venda > 500:
            qtd += 1
            soma += venda
    resultado = {"quantidade": qtd,
                 "soma": soma}
    return resultado
vendas = [100, 600, 800, 300, 900]
resultado = analisar_vendas(vendas)
print(resultado)