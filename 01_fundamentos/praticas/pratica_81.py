#pratica 80 dicionarios + logica 
funcionarios = {
    "João": 2800,
    "Maria": 4200,
    "Carlos": 1900,
    "Ana": 3500,
    "Pedro": 2400,
    "Lucas": 5000
}
qtd = 0
soma = 0
media = 0 
maior = None
nome = None
for chave in funcionarios:
    if funcionarios[chave] >= 2500:
        qtd = qtd + 1
        soma = soma + funcionarios[chave]
        if maior is None:
            maior = funcionarios[chave]
            nome = chave
        elif funcionarios[chave] > maior:
            maior = funcionarios[chave]
            nome = chave
media = soma / qtd 
print(qtd, soma, media, maior, nome)