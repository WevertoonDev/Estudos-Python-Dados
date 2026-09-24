#pratica 166 funcao mais lista mais multiplas informacoes
def analisar_vendas(lista):
    qtd_m = 0
    soma = 0
    for i in range(len(lista)):
        if lista[i] >= 2000:
            qtd_m = qtd_m + 1
            soma = soma + lista[i]
    return soma
resultado = analisar_vendas([1500, 2200, 1800, 3000, 2500])
print(resultado)