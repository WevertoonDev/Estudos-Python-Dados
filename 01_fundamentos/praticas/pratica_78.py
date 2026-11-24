#pratica 77
vendas = {
    "João": 1200,
    "Maria": 3500,
    "Carlos": 1800,
    "Ana": 4200,
    "Pedro": 2700,
    "Lucas": 900
}
qtd = 0
soma = 0 
media = 0
menor = None
nome = None
for chave in vendas:
    if vendas[chave] < 2000:
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