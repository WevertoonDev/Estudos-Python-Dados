#Pratica_160
def analisar_numeros(lista):
    qtd = 0
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
        if lista[i] > 10:
            qtd = qtd + 1
    return soma 
resultado = analisar_numeros([5, 12, 8, 20, 15])
print(resultado,)
