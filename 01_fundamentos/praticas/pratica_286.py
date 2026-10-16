#pratica_286 analise de vendas
def analisar_vendas(vendas):
    total = 0
    for chave in vendas:
        total_t = chave["preco"] * chave["quantidade"]
        total = total + total_t
    resultado = {"Total_dos_produtos": total}  
    return resultado
vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 3},
    {"produto": "Teclado", "preco": 120, "quantidade": 2},
    {"produto": "Monitor", "preco": 800, "quantidade": 1},
    {"produto": "Headset", "preco": 150, "quantidade": 4}
]
resultado = analisar_vendas(vendas)
print(resultado)