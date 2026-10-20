#pratica 294
def contar_produtos(vendas):
    qtd = 0
    for item in vendas:
        if item["quantidade"] >= 3 and item["preco"] <200:
            qtd = qtd + 1
    resultado = {"quantidade_produtos": qtd}
    return resultado
vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 2},
    {"produto": "Teclado", "preco": 120, "quantidade": 5},
    {"produto": "Headset", "preco": 80, "quantidade": 3},
    {"produto": "Monitor", "preco": 400, "quantidade": 6}
]
resultado = contar_produtos(vendas)
print(resultado)