#pratica 89 um pouco mais livre 
alunos = {
    "João": 7.5,
    "Maria": 9.0,
    "Carlos": 5.5,
    "Ana": 8.0,
    "Pedro": 6.0,
    "Lucas": 4.5,
    "Julia": 8.5
}
qtd = 0
soma = 0
media = 0
qtd_a = 0
maior = None
nome = None
menor = None
nome_m = None
for chave in alunos:
    if alunos[chave] >= 6:
        qtd = qtd + 1
        soma = soma + alunos[chave]
media = soma / qtd
for chave in alunos:
    if alunos[chave] >= 6:
        if alunos[chave] > media:
            qtd_a = qtd_a + 1
        if maior is None:
            maior = alunos[chave]
            nome = chave
        elif alunos[chave] > maior:
            maior = alunos[chave]
            nome = chave
        if menor is None:
            menor = alunos[chave]
            nome_m = chave
        elif alunos[chave] < menor:
            menor = alunos[chave]
            nome_m = chave
print(qtd, soma, media, qtd_a, maior, nome, menor, nome_m)