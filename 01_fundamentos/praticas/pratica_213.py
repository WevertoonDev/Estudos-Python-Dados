#pratica 213 exemplo
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"


try:
    idade = int(input("Digite sua idade: "))
    resultado = verificar_idade(idade)
    print(resultado)

except:
    print("Digite uma idade válida.")
#pratica 213
def verificar_idade(idade):
    if idade >= 18:
        return("Maior de idade")
    else:
        return("Menor de idade")
try:
    idade = int(input("Digite sua idade: "))
    resultado = verificar_idade(idade)
    print(resultado)
except:
    print("Idade inválida")