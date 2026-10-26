#aula 03 Preparando_Dados_De_Uma_Loja
produtos = [
    " Mouse ",
    "TECLADO",
    "mouse",
    " Monitor ",
    "teclado "
]
produtos_limpos = []
for produto in produtos:
    nome = produto.strip().lower()
    produtos_limpos.append(nome)
produtos_limpos = set(produtos_limpos)
print(len(produtos_limpos))