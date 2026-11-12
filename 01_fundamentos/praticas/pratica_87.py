#pratica 87 filtro + media + extremos
produtos = {
    "Arroz": 25,
    "Feijão": 18,
    "Café": 32,
    "Macarrão": 12,
    "Açúcar": 20,
    "Farinha": 15,
    "Leite": 28
}
qtd = 0
soma = 0 
media = 0
qtd_a = 0
maior = None
nome = None
menor = None
nome_m = None
for chave in produtos:
    if produtos[chave] >= 18:
        qtd = qtd + 1
        soma = soma + produtos[chave]
media = soma / qtd
for chave in produtos:
    if produtos[chave] >= 18:
        if produtos[chave] > media:
            qtd_a = qtd_a + 1
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
print(qtd, soma, media, qtd_a, maior, nome, menor, nome_m)