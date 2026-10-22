#pratica 297 enumate()
produto = "Teclado"
preco = 120
quantidade = 2
print(f"O faturamento do {produto} foi R$ {preco * quantidade}")
def listar_faturamento(vendas):
    for indice, item in enumerate(vendas, start=1):
        print(f"{indice}: {item['produto']} R$ {item['preco'] * item['quantidade']}")      
vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 3},
    {"produto": "Teclado", "preco": 120, "quantidade": 2},
    {"produto": "Monitor", "preco": 400, "quantidade": 2}
]
listar_faturamento(vendas)