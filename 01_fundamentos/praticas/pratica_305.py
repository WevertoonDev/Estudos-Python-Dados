#pratica 305 
def contar_vendas_altas(vendas):
    qtd = 0
    for numero in vendas:
        if numero > 500:
            qtd += 1
    resultado = {"Vendas acima de R$ 500": qtd}
    return resultado
vendas = [100, 600, 800, 300, 900]
resultado = contar_vendas_altas(vendas)
print(resultado)