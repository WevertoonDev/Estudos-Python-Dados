#pratica_293 vamos avancar
def contar_produtos_mais_vendidos(vendas):
    qtd = 0
    for item in vendas:
        if item["quantidade"] > 3:
            qtd = qtd + 1
    resultado = {"quantidade_produto": qtd}
    return resultado
vendas = [
    {"produto": "Mouse", "quantidade": 2},
    {"produto": "Teclado", "quantidade": 5},
    {"produto": "Headset", "quantidade": 3},
    {"produto": "Monitor", "quantidade": 6}
]
resultado = contar_produtos_mais_vendidos(vendas)
print(resultado)