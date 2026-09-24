#pratica 147 return + condicao
def verificar_idade(idade):
    if idade >= 18:
        return("Maior de idade")
    else:
        return("Menor de idade")
resultado = verificar_idade(20)
print(resultado)