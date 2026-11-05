#aula 27
vendas = [200, 250, 220, 220, 300]
for i in range(1,len(vendas)):
    diferenca = vendas[i] - vendas[i - 1]
    if diferenca > 0:
        print("Aumento")
    elif diferenca < 0:
        print("diminuiu")
    else:
        print("Permaneceu estável")