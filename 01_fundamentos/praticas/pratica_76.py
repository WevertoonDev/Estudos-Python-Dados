#pratica 75 dicionari + logica 
funcionarios = {
    "João": 2800,
    "Maria": 3500,
    "Carlos": 2200,
    "Ana": 4100,
    "Pedro": 1900,
    "Lucas": 3200
}
qtd = 0 
soma = 0 
media = 0 
nome = None
salario = None
for chave in funcionarios:
    if funcionarios[chave] >= 3000:
        qtd = qtd + 1
        soma = soma + funcionarios[chave]
        if salario is None:
            nome = chave
            salario = funcionarios[chave]
        elif funcionarios[chave] > salario:
            nome = chave
            salario = funcionarios[chave]
media = soma / qtd
print(qtd, soma, media, nome, salario)