#pratica 94 mudando o tipo de analise 
funcionarios = {
    "João": 2400,
    "Maria": 3200,
    "Carlos": 2800,
    "Ana": 4500,
    "Pedro": 2600,
    "Lucas": 1900,
    "Julia": 3700
}
qtd = 0
soma = 0
media  = 0
qtd_m = 0
qtd_a = 0
maior = None
nome = None
menor = None
nome_m = None
dif = None
for chave in funcionarios:
    if funcionarios[chave] >= 2500:
        qtd = qtd + 1
        soma = soma + funcionarios[chave]
media = soma / qtd
for chave in funcionarios:
    if funcionarios[chave] >= 2500:
        if funcionarios[chave] > media:
            qtd_a = qtd_a + 1
        if funcionarios[chave] == media:
            qtd_m = qtd_m + 1
        if maior is None:
            maior = funcionarios[chave]
            nome = chave
        elif  funcionarios[chave] > maior:
            maior = funcionarios[chave]
            nome = chave
        if menor is None:
            menor = funcionarios[chave]
            nome_m = chave
        elif funcionarios[chave] < menor:
            menor = funcionarios[chave]
            nome_m = chave
dif = maior - menor
print( qtd, soma, media, qtd_m, qtd_a, maior, nome, menor, nome_m, dif)