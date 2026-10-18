#Pratica_291_Novo_Conceito_Contar_Itens_Com_Uma_Codinção
def contar_vendas_altas(vendas):
    qtd = 0
    for chave in vendas:
        total = chave["preco"] * chave["quantidade"]
        if total > 200:
            qtd = qtd + 1
    resultado = {"Produto_caros": qtd}
    return resultado
vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 2},
    {"produto": "Teclado", "preco": 100, "quantidade": 3},
    {"produto": "Headset", "preco": 80, "quantidade": 1},
    {"produto": "Monitor", "preco": 400, "quantidade": 2}
]
resultado = contar_vendas_altas(vendas)
print(resultado)