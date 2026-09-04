produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 1200}
]
def produtos_promocao(produtos):
    nova_lista = []
    for produto in produtos:
        if produto["preco"] > 100:
            nova_lista.append(produto)
    return nova_lista
