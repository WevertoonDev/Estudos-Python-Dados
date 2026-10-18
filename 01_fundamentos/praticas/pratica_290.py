#pratica 290 Novo_Conceito_Encontrar_o_Maior_Valor
def maior_faturamento(vendas):
    maior = None
    nome = ""
    for chave in vendas:
        total = chave["preco"] * chave["quantidade"]
        if maior is None:
            maior = total
            nome = chave["produto"]
        elif total > maior:
            maior = total
            nome = chave["produto"]
    resultado ={"maior_faturamento": maior,
                "nome_produto": nome}
    return resultado
vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 2},
    {"produto": "Teclado", "preco": 100, "quantidade": 3},
    {"produto": "Headset", "preco": 80, "quantidade": 1}
]
resultado = maior_faturamento(vendas)
print(resultado)