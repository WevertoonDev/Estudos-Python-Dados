#pratica 154
def classificar_compra(valor):
    if valor >= 500:
        return("Compra grande")
    else:
        return("Compra normal")
resultado = classificar_compra(valor = 350)
print(resultado)
#pratica 154 tentativa 2
def classificar_idade(idade):
    if idade >= 18:
        return("Adulto")
    else:
        return("Menor de idade")
resultado = classificar_idade(idade = 16)
print(resultado)