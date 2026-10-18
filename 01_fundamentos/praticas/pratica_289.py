#pratica_289 somando valores de uma lista 
def calcular_faturamento(vendas):
    preco_final = 0
    for chave in vendas:
        total = chave["preco"] * chave["quantidade"]
        preco_final = preco_final + total
    resultado = {"Preço_Final": preco_final}
    return resultado
vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 2},
    {"produto": "Teclado", "preco": 100, "quantidade": 3},
    {"produto": "Headset", "preco": 80, "quantidade": 1}
]
resultado = calcular_faturamento(vendas)
print(resultado)