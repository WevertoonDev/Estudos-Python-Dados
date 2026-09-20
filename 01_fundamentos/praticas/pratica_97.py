#prartica 97 ultima verificaçao de logica
idades = {
    "João": 17,
    "Maria": 25,
    "Carlos": 32,
    "Ana": 19,
    "Pedro": 41,
    "Lucas": 28,
    "Julia": 15
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
dif = None
for chave in idades:
    if idades[chave] >= 18:
        qtd = qtd + 1
        soma = soma + idades[chave]
media = soma / qtd
for chave in idades:
    if idades[chave] >= 18:
        if idades[chave] > media:
            qtd_a = qtd_a + 1
        if idades[chave] < media:
            qtd_b = qtd_b + 1
        if maior is None:
            maior = idades[chave]
            nome = chave
        elif idades[chave] > maior:
            maior = idades[chave]
            nome = chave
        if menor is None:
            menor = idades[chave]
            nome_m = chave
        elif idades[chave] < menor:
            menor = idades[chave]
            nome_m = chave
dif = maior - menor
print(qtd, soma, media, qtd_a, qtd_b, maior, nome, menor, nome_m, dif)