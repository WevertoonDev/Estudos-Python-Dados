#pratica 295 
def somar_vendas_caras(vendas):
    somar = 0
    for produtos in vendas:
        if produtos["quantidade"] >= 3:
            total = produtos["preco"] * produtos["quantidade"]
            somar = somar + total
    resultado = {"faturamento": somar}
    return resultado
vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 2},
    {"produto": "Teclado", "preco": 120, "quantidade": 5},
    {"produto": "Headset", "preco": 80, "quantidade": 3},
    {"produto": "Monitor", "preco": 400, "quantidade": 6}
]
resultado = somar_vendas_caras(vendas)
print(resultado)