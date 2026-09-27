#pratica 206
def verificar_desconto(idade, valor):
    if idade >= 18 and valor >= 100:
        return("Desconto")
    else:
        return("Sem desconto")
idade = int(input("Digite sua idade: "))
valor = float(input("Qual foi o valor: "))
resultado = verificar_desconto(idade, valor)
print(resultado)