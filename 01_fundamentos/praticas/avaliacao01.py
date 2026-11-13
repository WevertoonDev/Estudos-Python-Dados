vendas = [
    {"produto": "Notebook", "valor": 3500},
    {"produto": "Mouse", "valor": 150},
    {"produto": "Monitor", "valor": 1200},
    {"produto": "Teclado", "valor": 300},
    {"produto": "Celular", "valor": 2800}
]
qtd = 0
maior = None
nome = None
for venda in vendas:
    if venda["valor"] > 1000:
        qtd += 1
        if maior is None:
            maior = venda["valor"]
            nome = venda["produto"]
        elif venda["valor"] > maior:
            maior = venda["valor"]
            nome = venda["produto"]
print(qtd, maior, nome)