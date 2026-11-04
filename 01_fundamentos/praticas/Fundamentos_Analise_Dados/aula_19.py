#Aula_19_Identificando_o_Maior_Salto_nas_Vendas
vendas = [100, 120, 130, 150, 170, 180, 200, 500]
for i in range(1,len(vendas)):
    maior_salto = vendas[i] - vendas[i - 1]
    print(maior_salto)