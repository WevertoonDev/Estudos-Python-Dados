#pratica 82 dicionarios + logica 
vendas = {
    "João": 1800,
    "Maria": 3200,
    "Carlos": 2500,
    "Ana": 4100,
    "Pedro": 1500,
    "Lucas": 3800
}
qtd = 0
soma = 0
media = 0
abaixo_m = 0
nome_m = None
maior = None
for chave in vendas:
    if vendas[chave] >= 2500:
        qtd = qtd + 1
        soma = soma + vendas[chave]
media = soma / qtd
for chave in vendas:
    if vendas[ chave] >= 2500:
        if vendas[chave] < media:
            abaixo_m = abaixo_m + 1
        if maior is None:
            maior = vendas[chave]
            nome_m = chave
        elif vendas[chave] > maior:
            maior = vendas[chave]
            nome_m = chave
print(qtd, soma, media, abaixo_m, nome_m, maior)