vendas = [100, 120, 130, 150, 170, 180, 200, 500, 900]

diferencas = []

for i in range(1, len(vendas)):
    diferenca = vendas[i] - vendas[i - 1]
    diferencas.append(diferenca)
maior = diferencas[0]

for valor in diferencas:
    if valor > maior:
        maior = valor

print(diferencas)
print(f"Maior salto: {maior}")