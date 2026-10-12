#pratica 93 filtro mais analise completa 
alunos = {
    "João": 5.0,
    "Maria": 8.5,
    "Carlos": 6.0,
    "Ana": 9.5,
    "Pedro": 7.0,
    "Lucas": 4.5,
    "Julia": 8.0
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
for chave in alunos:
    if alunos[chave] >= 6:
        qtd = qtd + 1
        soma = soma + alunos[chave]
media = soma / qtd
for chave in alunos:
    if alunos[chave] >= 6:
        if alunos[chave] > media:
            qtd_a = qtd_a + 1
        if alunos[chave] < media:
            qtd_b = qtd_b + 1
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
dif = maior - menor
print(qtd, soma, media, qtd_a, qtd_b, maior, nome, menor, nome_m, dif)