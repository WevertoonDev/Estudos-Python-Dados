#Pratica_283
def analisar_notas(notas):
    total = 0
    soma_t = 0
    qtd = 0
    nome = None
    maior = None
    qtd_b = 0
    for chave in notas:
        total = total + 1
        soma_t = soma_t + chave["nota"]
        if chave["nota"] >= 7:
            qtd = qtd + 1
        if chave["nota"] < 7:
            qtd_b = qtd_b + 1
        if maior is None:
            maior = chave["nota"]
            nome = chave["aluno"]
        elif chave["nota"] > maior:
            maior = chave["nota"]
            nome = chave["aluno"]
    media = soma_t / total
    resultado = {"media": media,
                 "aprovados": qtd,
                 "melhor_aluno": nome,
                 "abaixo_da_media": qtd_b}
    return resultado
notas = [
    {"aluno": "Ana", "nota": 8},
    {"aluno": "Pedro", "nota": 6},
    {"aluno": "Julia", "nota": 10},
    {"aluno": "Carlos", "nota": 4}
]
resultado = analisar_notas(notas)
print(resultado)