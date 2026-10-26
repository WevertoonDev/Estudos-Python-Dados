#Aula_01_Preparando_dados_com_python
produtos = [" Mouse ", "TECLADO ", " monitor"]
produtos_limpos = []
for produto in produtos:
    nome = produto.strip().lower()
    produtos_limpos.append(nome)
print(produtos_limpos)