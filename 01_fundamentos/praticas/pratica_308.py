#pratica 308
def encontrar_maior_faturamento(vendas):
    maior_faturamento = 0
    produto_destaque = None
    for item in vendas:
        faturamento = item["preco"] * item["quantidade"]
        if faturamento > maior_faturamento:
            maior_faturamento = faturamento
            produto_destaque = item["produto"]
    return {"produto": produto_destaque,
            "faturamento": maior_faturamento}
vendas = [
    {"produto": "Mouse", "quantidade": 10, "preco": 50},
    {"produto": "Teclado", "quantidade": 5, "preco": 100},
    {"produto": "Monitor", "quantidade": 3, "preco": 300}
]
resultado = encontrar_maior_faturamento(vendas)
print(resultado)