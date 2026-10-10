#pratica 281
def gerar_relatorio(vendas):
    total_v = 0
    qtd = 0
    nome = None
    maior = None
    qtd_a = 0
    for chave in vendas:
        total = chave["preco"] * chave["quantidade"]
        total_v = total_v + total
        qtd = qtd + 1
        if maior is None:
            maior = chave["quantidade"]
            nome = chave["produto"]
        elif chave["quantidade"] > maior:
            maior = chave["quantidade"]
            nome = chave["produto"]
        if chave["preco"] > 200:
            qtd_a = qtd_a + 1
        resultado = {"Total_vendas": total_v,
                     "Quantidade_produtos": qtd,
                     "Produto_mais_vendido": nome,
                     "Vendas_acima_200": qtd_a}
    return resultado
vendas = [
    {"produto": "Teclado", "preco": 100, "quantidade": 2},
    {"produto": "Mouse", "preco": 50, "quantidade": 3},
    {"produto": "Monitor", "preco": 800, "quantidade": 1},
    {"produto": "Headset", "preco": 150, "quantidade": 2}
]
resultado = gerar_relatorio(vendas)
print(resultado)