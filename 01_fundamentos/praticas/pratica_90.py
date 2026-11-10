#Pratica_90_Consolidando_Tudo
funcionarios = {
    "João": 2200,
    "Maria": 3800,
    "Carlos": 2700,
    "Ana": 4500,
    "Pedro": 3100,
    "Lucas": 1900,
    "Julia": 2900
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
dif = 0
for chave in funcionarios:
    if funcionarios[chave] >= 2500:
        qtd = qtd + 1
        soma = soma + funcionarios[chave]
media = soma / qtd
for chave in funcionarios:
    if funcionarios[chave] >= 2500:
        if funcionarios[chave] > media:
            qtd_a = qtd_a + 1
        if funcionarios[chave] < media:
            qtd_b = qtd_b + 1
        if maior is None:
            maior = funcionarios[chave]
            nome = chave
        elif funcionarios[chave] > maior:
            maior = funcionarios[chave]
            nome = chave
        if menor is None:
            menor = funcionarios[chave]
            nome_m = chave
        elif funcionarios[chave] < menor:
            menor = funcionarios[chave]
            nome_m = chave
dif = maior - menor 
print(qtd, soma, media, qtd_a, qtd_b, maior, nome, menor, nome_m, dif)