#pratica 84 dicionario + filtro + media + menor valor
vendas = {
    "João": 1800,
    "Maria": 3200,
    "Carlos": 2500,
    "Ana": 4100,
    "Pedro": 1500,
    "Lucas": 2800
}
qtd = 0 
soma = 0
media = 0
menor = None
nome = None
for chave in vendas:
    if vendas[chave] >= 2500:
        qtd = qtd + 1
        soma = soma + vendas[chave]
        if menor is None:
            menor = vendas[chave]
            nome = chave 
        elif vendas[chave] < menor:
            menor = vendas[chave]
            nome = chave
media = soma / qtd
print(qtd, soma, media, menor, nome)