#aula 28
diferencas = [50, -30, 0, 80, -20, 0, 40]
aumento = 0
diminuicao = 0
estavel = 0
for numero in diferencas:
    if numero > 0:
        aumento = aumento + 1
    elif numero < 0:
        diminuicao = diminuicao + 1
    else:
        estavel = estavel + 1
print(f"Aumentaram: {aumento}, diminuiram: {diminuicao} e ficaram estaveis: {estavel}")