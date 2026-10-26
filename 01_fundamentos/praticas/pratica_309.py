#pratica 309 
def classificar_produtos(vendas):
    resultado = []
    for item in vendas:
        faturamento = item["preco"] * item["quantidade"]
        if faturamento >= 500:
            classificacao = "Bom desempenho"
        else:
            classificacao = "Baixo desempenho"
        resultado.append({"produto": item["produto"],
                          "faturamento": faturamento,
                          "classificacao": classificacao})
    return resultado
vendas = [
    {"produto": "Mouse", "quantidade": 10, "preco": 50},
    {"produto": "Teclado", "quantidade": 3, "preco": 100},
    {"produto": "Monitor", "quantidade": 3, "preco": 300}
]
resultado = classificar_produtos(vendas)
print(resultado)