#pratica 96 revisao final antes do input()
produtos = {
    "Arroz": 12,
    "Feijão": 7,
    "Café": 18,
    "Macarrão": 25,
    "Açúcar": 5,
    "Farinha": 10,
    "Biscoito": 20
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
for chave in produtos:
    if produtos[chave] >= 10:
        qtd = qtd + 1
        soma = soma + produtos[chave]
media = soma / qtd
for chave in produtos:
    if produtos[chave] >= 10:
        if produtos[chave] > media:
            qtd_a = qtd_a + 1
        if produtos[chave] < media:
            qtd_b = qtd_b + 1
        if produtos[chave] == media:
            qtd_i = qtd_i + 1
        if maior is None:
            maior = produtos[chave]
            nome = chave
        elif produtos[chave] > maior:
            maior = produtos[chave]
            nome = chave
        if menor is None:
            menor = produtos[chave]
            nome_m = chave
        elif produtos[chave] < menor:
            menor = produtos[chave]
            nome_m = chave
dif = maior - menor
print(qtd, soma, media, qtd_a, qtd_b, qtd_i, maior, nome, menor, nome_m, dif)