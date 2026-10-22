#pratica 296
def listar_vendas(vendas):
    for indice, venda in enumerate(vendas, start=1):
        print(f"Venda {indice}: {venda['produto']} - Quantidade: {venda['quantidade']}")
vendas = [
    {"produto": "Mouse", "quantidade": 3},
    {"produto": "Teclado", "quantidade": 5},
    {"produto": "Monitor", "quantidade": 2}
]
resultado = listar_vendas(vendas)
print(resultado)