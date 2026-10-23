#pratica 300
vendas = [
    {"produto": "Cadeira", "preco": 250, "quantidade": 2},
    {"produto": "Mesa", "preco": 400, "quantidade": 3},
    {"produto": "Luminária", "preco": 80, "quantidade": 4}
]
total = 0
for item in vendas:
    faturamento = item["preco"] * item["quantidade"]
    total += faturamento
print(f"O faturamento total é de R$ {total}")