#pratica 79 dicionarios + logica
estoque = {
    "Arroz": 12,
    "Feijão": 25,
    "Café": 7,
    "Macarrão": 30,
    "Açúcar": 4,
    "Farinha": 18
}
qtd = 0 
soma = 0
media = 0 
menor = None
nome = None
for chave in estoque:
    if estoque[chave] < 10:
        qtd = qtd + 1
        soma = soma +estoque[chave]
        if menor is None:
            menor = estoque[chave]
            nome = chave
        elif estoque[chave] < menor:
            menor = estoque[chave]
            nome = chave 
media = soma / qtd
print(qtd, soma, media, menor, nome)