#Pratica_185_Funções_Trabalhando_com_Lista
def analisar_vendas(lista):
    qtd = 0
    soma = 0
    for numero in lista:
        if numero >= 2000:
            qtd = qtd + 1
            soma = soma + numero
    media = soma / qtd 
    return media 
resultado = analisar_vendas(lista=[1500, 2200, 1800, 3000, 2500, 1000])
print(resultado)