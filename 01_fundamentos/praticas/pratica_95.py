#pratica 95 revisao de logica 
vendas = {
    "João": 1200,
    "Maria": 2800,
    "Carlos": 3500,
    "Ana": 1800,
    "Pedro": 4200,
    "Lucas": 2500,
    "Julia": 3100
}
qtd = 0
soma = 0
media = 0
qtd_a = 0
qtd_b = 0
qtd_i = 0
maior = None
nome = None
menor = None
nome_m = None
dif = None
for chave in vendas:
    if vendas[chave] >= 2500:
        qtd = qtd + 1
        soma = soma + vendas[chave]
media = soma / qtd 
for chave in vendas:
    if vendas[chave] >= 2500:
        if vendas[chave] > media:
            qtd_a = qtd_a + 1
        if vendas[chave] < media:
            qtd_b = qtd_b + 1
        if vendas[chave] == media:
            qtd_i = qtd_i + 1
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
dif = maior - menor
print(qtd, soma, media, qtd_a, qtd_b, qtd_i, maior, nome, menor, nome_m, dif)