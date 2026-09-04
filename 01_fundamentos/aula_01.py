# aula 01 Fundamentos exercicio 1
print("Meu nome é Weverton," \
"Estou estudando Python, " \
"Quero trabalhar com programação")

# exercicio 02
nome = "Weverton"
idade = 29
profissao = "programador"
print(nome, idade, profissao)

# exercicio 03
nome = "Weverton"
idade = 29
profissao = "programador"
print("Meu nome é",nome, "e tenho", idade, "anos e quero ser", profissao)

#aula 02 exercicio 04 
nome = "Weverton"
idade = 29
altura = 1.80
estudando = True
print(type(nome), 
      type(idade), 
      type(altura), 
      type(estudando))

#aula 3 — Operações matemáticas exercício 05
# soma = + exemplo 10 + 2 = 12
# subtração = - exemplo 10 - 2 = 8
# multiplicação = * exemplo 10 * 2 = 20
# divisão / exemplo 10 / 2 = 5.0
preco = 10 
quantidade = 5
resultado = preco * quantidade
print("O resultado é ,", resultado)

# exercício 06 
valor = 100
pessoas = 4
resultado = valor / pessoas
print("O resultado por pessoa é ,", resultado)

# exercício 07
numero = 17
divisor = 5
restultado = numero % divisor
resto = resultado 
print("O resto da divisao é ,", resto)

#aula 4 - Comparaçções exercicio 08
idade = 29
print(idade > 18,
      idade == 29,
      idade < 18)

# exercicio 09
idade = 29
if idade >= 18:
    print("É maior de idade")

# exercicio 10
idade = 16 
if idade >= 18:
    print("É maior de idade")
else:
    print("Menor de idade ")

# exercicio 11
nota = 7
if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# exercicio 12
nota = 6
if nota >= 7:
    print("Aprovado")
elif nota >= 5 and nota <= 6.9:
    print("Recuperação")
else:
    print("Reprovado")

# exercicio 13
idade = 29
if idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")

#aula 6 - or exercicio 14 entrada permitida
idade = 13
if idade <= 12 or idade >= 60:
    print("Faixa prioritaria")
else:
    print("Faixa comum")

#exercicio 15 - not 
idade = 16
if not idade >= 18:
    print("menor de idade ")
else:
    print("maior de idade")

# aula 7 - while exercicio 16 contador
contador = 0
while contador < 5:
    contador = contador +1
    print(contador)

# exerciocio 17 contagem regressiva
contador = 6
while contador > 1:
    contador = contador - 1
    print(contador)
print("Fim!")
    
   
