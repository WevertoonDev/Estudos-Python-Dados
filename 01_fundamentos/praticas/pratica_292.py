#prtica 292
def produto_mais_vendido(vendas):
    mais_vendido = 0
    nome = ""
    for chave in vendas:
         if chave["quantidade"] > mais_vendido:
            mais_vendido = chave["quantidade"]
            nome = chave["produto"]
    resultado = {"produto": nome,
                 "quantidade": mais_vendido}
    return resultado
vendas = [
    {"produto": "Mouse", "quantidade": 2},
    {"produto": "Teclado", "quantidade": 5},
    {"produto": "Headset", "quantidade": 3}
]
resultado = produto_mais_vendido(vendas)
print(resultado)