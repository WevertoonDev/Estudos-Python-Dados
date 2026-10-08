#Pratica_281_Mini_Projeto
def gerar_relatorio(produtos):
    qtd = 0
    soma_t = 0
    mais_c = None
    nome = None
    maior_q = None
    nome_q = None
    for chave in produtos:
        qtd = qtd + 1
        total =chave["preco"] * chave["quantidade"]
        soma_t = soma_t + total
        if mais_c is None:
            mais_c = chave["preco"]
            nome = chave["nome"]
        elif chave["preco"] > mais_c:
            mais_c = chave["preco"]
            nome = chave["nome"]
        if maior_q is None:
            maior_q = chave["quantidade"]
            nome_q = chave["nome"]
        elif chave["quantidade"] > maior_q:
            maior_q = chave["quantidade"]
            nome_q = chave["nome"]
    resultado = {"Total_produtos": qtd,
                 "Valor_estoque": soma_t,
                 "Produto_mais_caro": nome,
                 "Maior_estoque": nome_q}
    return resultado
produtos = [
    {"nome": "Arroz", "preco": 25, "quantidade": 2},
    {"nome": "Feijão", "preco": 8, "quantidade": 3},
    {"nome": "Café", "preco": 18, "quantidade": 1},
    {"nome": "Macarrão", "preco": 6, "quantidade": 4}]
resultado = gerar_relatorio(produtos)
print(resultado)