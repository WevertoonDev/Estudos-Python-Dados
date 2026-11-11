#pratica 88 filtro mais media mais contagem
vendas = {
    "João": 1200,
    "Maria": 3500,
    "Carlos": 2800,
    "Ana": 1900,
    "Pedro": 4200,
    "Lucas": 2600,
    "Julia": 1700
}
qtd = 0
soma = 0
media = 0
qtd_a = 0
qtd_b = 0
maior = None
nome = None
menor = None
nome_m = None
for chave in vendas:
    if vendas[chave] >= 2000:
        qtd = qtd + 1
        soma = soma + vendas[chave]
media = soma / qtd
for chave in vendas:
    if vendas[chave] >= 2000:
        if vendas[chave] > media:
            qtd_a = qtd_a + 1
        if vendas[chave] < media:
            qtd_b = qtd_b + 1
        if maior is None:
            maior = vendas[chave]
            nome = chave
        elif vendas[chave] > maior:
            maior = vendas[chave]
            nome = chave
        if menor is None:
            menor = vendas[chave]
            nome_m = chave
        elif vendas[chave] < menor:
            menor = vendas[chave]
            nome_m = chave
print(qtd, soma, media, qtd_a, qtd_b, maior, nome, menor, nome_m)