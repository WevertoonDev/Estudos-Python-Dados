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

#exeercicio 18 while +acumulador
acumulador = 0
contador = 0
while contador < 5:
    contador = contador + 1
    acumulador = acumulador + contador
print(acumulador)

# exercicio 19 -contar de 1 ate 10
contador = 0
while contador < 10:
    contador = contador +  1
    print(contador)

# exercicio 20 - soma ate 10
soma = 0
contador = 0
while contador < 10:
    contador = contador + 1
    soma = soma + contador
print(soma)

# aula 8 - for - pratica 1
for numero in range(1,11):
    print(numero)

# aula 8 - for - pratica 2
for numero in range(2, 11, 2):
    print(numero)

# exercicio 21 - soma com for
soma = 0 
contador = 0
for contador in range(1, 11):
    soma = soma + contador 
print(soma)

# exercicio 22 - um pequeno desafio
for numero in range(1,11,2):
    print(numero)

# exercicio 23 - tabuada
soma = 0
for soma in range(1,11):
    print(soma * 5)

# exercicio 24 - tabuada escolhida 
for tabuada in range(1,11):
    print(tabuada * 7)
print("fim da tabuada do 7")

#exercicio 25 - for dentro de for
for tabuada in range(1,6):
    for numero in range(1,11):
        print(tabuada * numero)

# aula 9 - lista -pratica 1
animais = ["cachorro", "gato", "leão"]
print(animais[1])

#pratica 2
notas = [7, 8, 9, 10]
print(notas[2])

#pratica 3
frutas = ["maçã", "banana", "laranja"]
frutas[1] = "uva"
print(frutas[1])

#pratica 4 
frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(fruta)

#pratica 5
frutas = ["maçã", "banana"]
frutas.append("laranja"),
frutas.append("uva")
print(frutas)

#pratica 6
notas = [7, 8, 9, 10, 6]
print(len(notas))

#pratica 7 
notas = [7, 8, 9, 10, 6]
for i in range(len(notas)):
    print(notas[i])

#pratica 8 
frutas = ["maçã", "banana", "laranja", "uva"]
for i in range(len(frutas)):
    print(i, frutas[i])

#pratica 9
notas = [7, 5, 9, 6, 10]
for i in range(len(notas)):
    print(i, notas[i])

#pratica 10 
notas = [5, 6, 7, 8]
for i in range(len(notas)):
    notas[i] = notas[i] + 1
print(notas)

#pratica 10 - finalizacao
notas = [5, 6, 7, 8]
for i in range(len(notas)):
    notas[i] = notas[i] + 2
print(notas)
#pratica
numeros = [10, 20, 30, 40]
numeros.remove(30)
print(numeros)