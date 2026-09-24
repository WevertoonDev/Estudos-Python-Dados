#pratica 151 return mais calculo mais condicao
def verificar_desconto(idade, valor):
    if idade >= 18 and valor >= 100:
        return("Desconto")
    else:
        return("Sem desconto")
resultado = verificar_desconto(idade = 20, valor = 150)
print(resultado)