#Pratica_280_Lista_+_Dicionários
def analisar_produtos(produtos):
    qtd = 0
    mais_c = None
    nome = None
    mais_b = None
    nome_b = None
    soma = 0
    for chave in produtos:
        qtd = qtd + 1
        soma = soma + chave["preco"]
        if mais_c is None:
            mais_c = chave["preco"]
            nome = chave["nome"]
        elif chave["preco"] > mais_c:
            mais_c = chave["preco"]
            nome = chave["nome"]
        if mais_b is None:
            mais_b = chave["preco"]
            nome_b = chave["nome"]
        elif chave["preco"] < mais_b:
            mais_b = chave["preco"]
            nome_b = chave["nome"]
    resultado = {"Quantidade": qtd,
                 "Mais_caro": nome,
                 "Mais_barato": nome_b,
                 "Preço_total": soma}
    return resultado
produto = [
    {"nome": "Arroz", "preco": 25},
    {"nome": "Feijão", "preco": 8},
    {"nome": "Café", "preco": 18},
    {"nome": "Macarrão", "preco": 6}]
resultado = analisar_produtos(produto)
print(resultado)