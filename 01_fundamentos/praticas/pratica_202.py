#pratica 202 integracao input mais funcao
idade = int(input("Digite sua idade: "))
def verificar_idade(idade):
    if idade >= 18:
        return("Maior de idade")
    else:
        return("Menor de idade")
resultado = verificar_idade(idade)
print(resultado)
