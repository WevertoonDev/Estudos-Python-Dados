faturamento_produto = 300
faturamento_total = 1500
percentual = (faturamento_produto / faturamento_total) * 100
print("Participação no faturamento:", percentual,"%")

#for chave in vendas:
#    total = chave["preco"] * chave["quantidade"]
#   percentual = (total / total_t) * 100 

#pratica_285
def analisar_vendas(vendas):
    total_t = 0
    nome = 0
    maior = None
    soma = 0
    qtd_a = 0
    for chave in vendas:
        total = chave["preco"] * chave["quantidade"]
        total_t = total_t + total
        soma = soma + chave["quantidade"]
        if maior is None:
            maior = chave["quantidade"]
            nome = chave["produto"]
        elif chave["quantidade"] > maior:
            maior = chave["quantidade"]
            nome = chave["produto"]
        if total > 500:
            qtd_a = qtd_a + 1
    participacao = {}
    for chave in vendas:
        total = chave["preco"] * chave["quantidade"]
        percentual = (total / total_t) * 100
        participacao[chave["produto"]] = percentual 
    resultado = {"total_vendido": total_t,
                 "produto_mais_vendido": nome,
                 "quantidade_total": soma,
                 "produtos_acima_500": qtd_a,
                 "percentual_produto": participacao}
    return resultado
vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 3},
    {"produto": "Teclado", "preco": 120, "quantidade": 2},
    {"produto": "Monitor", "preco": 800, "quantidade": 1},
    {"produto": "Headset", "preco": 150, "quantidade": 4}
]
resultado = analisar_vendas(vendas)
print(resultado)