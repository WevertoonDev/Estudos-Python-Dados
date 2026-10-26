#pratica 307
def analisar_participacao(vendas):
    total = 0
    for item in vendas:
        faturamento_t = item["preco"] * item["quantidade"]
        total += faturamento_t
    produto = []
    for item in vendas:
        faturamento_t = item["preco"] * item["quantidade"]
        participacao = (faturamento_t / total) * 100
        produto.append({"produto": item["produto"],
                        "participacao": round(participacao,2)})
    return{
        "faturamento_total": total,
        "produto": produto
    }
vendas = [
    {"produto": "Mouse", "quantidade": 10, "preco": 50},
    {"produto": "Teclado", "quantidade": 5, "preco": 100},
    {"produto": "Monitor", "quantidade": 3, "preco": 300}
]
resultado = analisar_participacao(vendas)
print(resultado)