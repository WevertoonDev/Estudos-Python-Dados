#pratica 148 return + caculo + condicao
def classificar_nota(nota):
    if nota >= 7:
        return("Aprovado")
    elif nota >= 5:
        return("Recuperação")
    else:
        return("Reprovado")
resultado = classificar_nota(8)
print(resultado)