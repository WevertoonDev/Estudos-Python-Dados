#pratica 83 dicionarios + logica 
produtos = {
    "Arroz": 25,
    "Feijão": 12,
    "Café": 8,
    "Macarrão": 30,
    "Açúcar": 5,
    "Farinha": 18
}
qtd = 0
soma = 0
media = 0
maior = None
nome = None
for chave in produtos:
    if produtos[chave] >= 10 and produtos[chave] <= 25:
        qtd = qtd + 1
        soma = soma + produtos[chave]
        if maior is None:
            maior = produtos[chave]
            nome = chave
        elif produtos[chave] > maior:
            maior = produtos[chave]
            nome = chave
media = soma / qtd
print(qtd, soma, media, maior, nome)

#pratica 83 dicionario mais logica
alunos = {
    "João": 5.5,
    "Maria": 8.0,
    "Carlos": 6.5,
    "Ana": 9.0,
    "Pedro": 4.0,
    "Lucas": 7.5
}
qtd = 0 
soma = 0
media = 0
maior = None
nome = None
for chave in alunos:
    if alunos[chave] >= 6 and alunos[chave] <= 8:
        qtd = qtd + 1
        soma = soma + alunos[chave]
        if maior is None:
            maior = alunos[chave]
            nome = chave
        elif alunos[chave] > maior:
            maior = alunos[chave]
            nome = chave 
media = soma / qtd 
print(qtd, soma, media, maior, nome)