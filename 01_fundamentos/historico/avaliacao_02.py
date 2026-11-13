gastos = [
    2172.54,
    3701.35,
    3518.09,
    3456.61,
    3249.38,
    2840.82,
    3891.45,
    3075.26,
    2317.64,
    3219.08
]
qtd = 0
qtd_t = 0
soma = 0
for gasto in gastos:
    qtd_t += 1
    if gasto > 3000:
        qtd += 1
        soma += gasto
faturamento = soma
total = qtd_t
porcetagem = (qtd / qtd_t)* 100
print(f"a quantidade é {qtd} e a porcetagem é {porcetagem:.2f}")