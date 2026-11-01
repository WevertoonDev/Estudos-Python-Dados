#Pratica_92_Dicionarios_+_Filtro_+_Analise
vendas = {
    "João": 1800,
    "Maria": 4200,
    "Carlos": 2600,
    "Ana": 3500,
    "Pedro": 2100,
    "Lucas": 4800,
    "Julia": 2900
}
qtd = 0
soma = 0
media = 0
qtd_m = 0
nome = None
maior = None
nome_m = None
menor = None
qtd_d = 0
for chave in vendas:
    if vendas[chave] >= 2500:
        qtd = qtd + 1
        soma = soma + vendas[chave]
media = soma / qtd 
for chave in vendas:
    if vendas[chave] >= 2500:
        if vendas[chave] > media:
            qtd_m = qtd_m + 1
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
qtd_d = maior - menor
print(qtd, soma, media, maior, nome, menor, nome_m, qtd_d)