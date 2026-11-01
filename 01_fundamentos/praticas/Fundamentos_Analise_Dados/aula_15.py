#Aula_15_Preparando_os_Dados
import numpy as np
vendas = [100, 120, 130, 150, 170, 180, 200, 500]
q1 = np.percentile(vendas, 25)
q3 = np.percentile(vendas, 75)
iqr = q3 - q1
limite_inferior = q1 - (1.5 * iqr)
limite_superior = q3 + (1.5 * iqr)
for venda in vendas:
    if venda < limite_inferior or venda > limite_superior:
        print(f"Possível outlier: {venda}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"IQR: {iqr}")
print(f"Q1: {q1}")
print(f"Q3: {q3}")