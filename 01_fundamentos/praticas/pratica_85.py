#Pratica_85_Filtro_+_Media_+_Acima_Abaixo_media
notas = {
    "João": 5.5,
    "Maria": 8.0,
    "Carlos": 6.5,
    "Ana": 9.0,
    "Pedro": 4.0,
    "Lucas": 7.5,
    "Julia": 6.0
}
qtd = 0
soma = 0
qtd_m = 0
media = 0
maior = None
nome = None
for chave in notas:
    if notas[chave] >= 6:
        qtd = qtd + 1 
        soma = soma + notas[chave]
media = soma / qtd 
for chave in notas:
    if notas[chave] >= 6:
        if notas[chave] > media:
            qtd_m = qtd_m + 1
            if maior is None:
                maior = notas[chave]
                nome = chave
            elif notas[chave] > maior:
                maior = notas[chave]
                nome = chave
print(qtd, soma, media, qtd_m, maior, nome)