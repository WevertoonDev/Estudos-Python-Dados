#pratica 86 filtro + media + menor valor
funcionarios = {
    "João": 2800,
    "Maria": 3500,
    "Carlos": 2200,
    "Ana": 4100,
    "Pedro": 3000,
    "Lucas": 1800,
    "Julia": 3900
}
qtd = 0 
soma = 0
media = 0
qtd_a = 0
menor = None
nome = None
for chave in funcionarios:
    if funcionarios[chave] >= 2500:
        qtd = qtd + 1
        soma = soma +funcionarios[chave]
media = soma / qtd 
for chave in funcionarios:
    if funcionarios[chave] >= 2500:
        if funcionarios[chave] < media:
            qtd_a = qtd_a + 1
            if menor is None:
                menor = funcionarios[chave]
                nome = chave
            elif funcionarios[chave] < menor:
                menor = funcionarios[chave]
                nome = chave
print(qtd, soma, media, qtd_a, menor, nome)