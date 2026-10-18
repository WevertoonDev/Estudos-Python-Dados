#pratica 288 tratando uma lista vazia
def analisar_vendas(vendas):
    nome = None
    maior = None
    for chave in vendas:
        total = chave["preco"] * chave["quantidade"]
        if maior is None:
            maior = total
            nome = chave["produto"]
        elif total > maior:
            maior = total
            nome = chave["produto"]
    if not vendas:
        return {}
    resultado = {"Nome_produto": nome,
                 "Valor_faturamento": maior}
    return resultado
vendas = [{"produto": "Mouse", "preco": 50, "quantidade": 3},
    {"produto": "Teclado", "preco": 120, "quantidade": 2},
    {"produto": "Monitor", "preco": 800, "quantidade": 1},
    {"produto": "Headset", "preco": 150, "quantidade": 4}]
resultado = analisar_vendas(vendas)
print(resultado)