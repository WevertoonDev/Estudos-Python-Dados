
#pratica 79 dicionario mais logica
notas = {
    "João": 8.5,
    "Maria": 6.0,
    "Carlos": 9.5,
    "Ana": 5.0,
    "Pedro": 7.0,
    "Lucas": 4.5
}
qtd = 0 
soma = 0
media = 0
menor = None
nome = None
for chave in notas:
    if notas[chave] < 7:
        qtd = qtd + 1 
        soma = soma + notas[chave]
        if menor is None:
            menor = notas[chave]
            nome = chave 
        elif notas[chave] < menor:
            menor = notas[chave]
            nome = chave
media = soma / qtd 
print(qtd, soma, media, menor, nome)