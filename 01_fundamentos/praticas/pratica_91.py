#pratica 91 dicionarios mais filtro mais duas analises
produtos = {
    "Arroz": 12,
    "Feijão": 25,
    "Café": 18,
    "Macarrão": 30,
    "Açúcar": 8,
    "Farinha": 22,
    "Leite": 15
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
qtd_d = 0
for chave in produtos:
    if produtos[chave] >= 15:
        qtd = qtd + 1
        soma = soma + produtos[chave]
media = soma / qtd
for chave in produtos:
    if produtos[chave] >= 15:
        if produtos[chave] > media:
            qtd_a = qtd_a + 1
        if produtos[chave] < media:
            qtd_b = qtd_b + 1
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
qtd_d = maior - menor
print(qtd, soma, media, qtd_a, qtd_b, maior, nome, menor, nome_m, qtd_d)