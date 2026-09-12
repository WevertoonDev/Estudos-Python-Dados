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

#pratica 3 trocar
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

#pratica 12 
compras = ["arroz", "feijão", "café"]
compras.append("leite")
compras.remove("arroz")
compras[0] = "macarrão"
print(compras)

#pratica 13 encontrando uma informarção na lista 
notas = [5, 8, 7, 10, 6]
soma = 0
for nota in notas:
    soma = soma + nota
print(soma)

#pratica 14 encontrar notas aprovados
notas = [5, 8, 7, 4, 10, 6]
for nota in notas:
    if nota >= 7:
        print(nota)

#pratica 15 contar aprovados
notas = [5, 8, 7, 4, 10, 6]
aprovado = 0
for nota in notas:
    if nota >= 7:
        aprovado = aprovado + 1
print(aprovado)

#pratica 16 maior nota
notas = [5, 8, 7, 4, 10, 6]
maior = 0
for nota in notas:
    if nota > maior:
        maior = nota
print(maior)

#pratica 17 
notas = [-5, -2, -8, -1]
maior = notas[0]
for nota in notas:
    if nota > maior :
        maior = nota 
print(maior)

#pratica 18 media da notas
notas = [6, 8, 7, 9, 10]
soma = 0
for nota in notas:
    soma = soma + nota
media = soma /len(notas)
print(soma,media)

#pratica 19 - contar notas acima da media 
notas = [5, 8, 7, 4, 10, 6]
soma = 0 
media = 0
qtd = 0 
for nota in notas:
    soma = soma + nota
media = soma /len(notas)
for nota in notas:
    if nota > media:
            qtd = qtd + 1
print(qtd)

#pratica 20 maior menor e media 
notas = [5, 8, 7, 4, 10, 6]
maior = notas[0]
menor = notas[0]
soma = 0
for nota in notas:
    soma = soma + nota
media = soma /len(notas)
for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota 
print(menor, media, maior)

#pratica 21 - notas aprovadas e media
notas = [5, 8, 7, 4, 10, 6, 9, 3]
maior = notas[0]
menor = notas[0]
qtd_media = 0 
soma = 0
for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    soma = soma + nota
media = soma /len(notas)
for nota in notas:
    if nota >= media:
        qtd_media = qtd_media + 1
print(menor, media, qtd_media, maior)

#pratica 22 - contar positivo e negativo
numeros = [5, -2, 8, -7, 10, -3, 4, -1]
positivo = 0
negativo = 0
for numero in numeros:
    if numero > 0:
        positivo = positivo + 1
    if numero < 0:
        negativo = negativo + 1
print(positivo, negativo)

#pratica 23 separar numeros pares e impares
numeros = [12, 7, 5, 8, 3, 10, 15, 2]
pares = 0
imapares = 0
for numero in numeros:
    if numero % 2==0:
        pares = pares + 1
    if numero % 2 == 1:
        imapares = imapares + 1
print(pares, imapares)

#pratica 24 encontrar numeros acima da media 
numeros = [10, 5, 8, 3, 12, 7, 15, 4]
acima_media = 0
soma = 0 
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
for numero in numeros:
    if numero > media:
        acima_media = numero
        print(acima_media)

#pratica 25 somar apenas os numeros pares 
numeros = [4, 7, 10, 3, 8, 5, 12, 1]
par = 0
for numero in numeros:
    if numero % 2 == 0:
        par = par + numero
print(par)

#pratica 26 somar apenas os numeros impares 
numeros = [3, 8, 11, 6, 7, 10, 15, 4]
impar = 0
for numero in numeros:
    if numero % 2 == 1:
        impar = impar + numero
print(impar)

#pratica 27 agora quero te pegar 
numeros = [5, -2, 8, -7, 10, -3, 4, -1, 12]
positivo = 0
negativo = 0
qtd_p = 0
qtd_n = 0
for numero in numeros:
    if numero > 0:
        positivo = positivo + numero
        qtd_p = qtd_p + 1
    if numero < 0:
        negativo = negativo + numero
        qtd_n = qtd_n +1 
print(positivo, negativo, qtd_p, qtd_n)

#pratica 28 o desafio do campeao kkk
numeros = [12, 5, 27, 8, 19, 3, 31, 14]
maior = numeros[0]
menor = numeros[0]
soma = 0
for numero in numeros:
    soma = soma +numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
media = soma / len(numeros)
print(menor, media, maior, soma )

#pratica 29 enocntrar um numero especifico
numeros = [12, 5, 27, 8, 19, 3, 31, 14]
alvo = 100
encontrou = False
for numero in numeros:
    if numero == alvo:
        encontrou = True
if encontrou:
    print("Encontrado")
else:
    print("Não encontrado!")

#pratica 30 procurar e contar 
numeros = [5, 8, 5, 10, 5, 3, 8, 5]
alvo = 5
qtd = 0
for numero in numeros:
    if numero == alvo:
        qtd = qtd + 1
print("o numero 5 aparece,",qtd)

#pratica 31 aora vamos complicar um pouquinho
numeros = [5, 8, 5, 10, 5, 3, 8, 5]
alvo = 5
for i in range(len(numeros)):
    if numeros[i] == alvo:
        print(i)

#pratica 32 encotarr posicoes e contar 
numeros = [5, 8, 5, 10, 5, 3, 8, 5]
alvo = 5
qtd = 0
for i in range(len(numeros)):
    if numeros[i] == alvo:
        qtd = qtd + 1
        print("Posição:", i)
print("Quantidade:", qtd)

#pratica 33 encontrando o maior numero e a posicao dele 
numeros = [12, 5, 27, 8, 19, 3, 31, 14]
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
for i in range(len(numeros)):
    if numeros[i] == maior:
        print(i, maior)

#pratica 34 maior numero e quantidade de vezes 
numeros = [7, 12, 5, 12, 3, 12, 8, 10]
maior = numeros[0]
qtd = 0
for numero in numeros:
    if numero > maior:
        maior = numero
for i in range(len(numeros)):
    if numeros[i] == maior:
        qtd = qtd + 1
print(qtd,maior)

#pratica 35 segundo maior numero
numeros = [12, 5, 27, 8, 19, 31, 14, 22]
maior = numeros[0]
segundo = numeros[0]
for numero in numeros:
    if numero > maior:
        segundo = maior
        maior = numero
    elif numero > segundo:
        segundo = numero
print(maior,segundo)

#pratica 36 maior e menor sem repetir for 
numeros = [15, 3, 27, 8, 19, 31, 6, 22]
maior = numeros[0]
menor = numeros[0]
p_maior = 0
p_menor = 0
for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        p_maior = i
    if numeros[i] < menor:
        menor = numeros[i]
        p_menor = i
print(p_menor, menor, p_maior, maior)

#pratica 37 soma a e posiçao
numeros = [10, 4, 7, 15, 3, 12, 8]
soma = 0
posicao = 0
maior = numeros[0]
for i in range(len(numeros)):
    soma = soma + numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i
print("a soma de todos sao:", soma,",o maior é", maior,"e a posicao é", posicao)

#pratica 38 maior menor e media 
numeros = [12, 5, 27, 8, 19, 3, 31, 14]
maior = numeros[0]
menor = numeros[0]
p_menor = 0
p_maior = 0
soma = 0
for i in range(len(numeros)):
    soma = soma + numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
        p_maior = i
    if numeros[i] < menor:
        menor = numeros[i]
        p_menor = i
media = soma /len(numeros)
print(soma, maior, p_maior, menor, p_menor, media)

#pratica 39 acima da media +posicao
numeros = [10, 5, 8, 3, 12, 7, 15, 4]
acima_media = 0
qtd = 0
posicao = 0
soma = 0
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
print(media)
for i in range(len(numeros)):
    if numeros[i] > media:
        acima_media = numeros[i]
        posicao = i
        qtd = qtd + 1
        print("Número:", numeros[i], "| Posição", i)
print("Quantidade:", qtd)

#pratica 40 vamos subir mais um nivel 
numeros = [18, 5, 27, 12, 9, 31, 6, 14, 3]
maior = numeros[0]
p_maior = 0
menor = numeros[0]
p_menor = 0
par = 0 
impar = 0 
for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        p_maior = i
    if numeros[i] < menor:
        menor = numeros[i]
        p_menor = i
    if numeros[i] % 2 == 0:
        par = par + 1
    if numeros[i] % 2 == 1:
        impar = impar +1
print(maior, p_maior, menor, p_menor, par, impar)

#pratica 41 soma dos pares  e dos impares
numeros = [4, 7, 10, 3, 8, 5, 12, 1, 6]
par = 0 
impar = 0
qtd_par = 0
qtd_impar = 0
for numero in numeros:
    if numero % 2 == 0:
        par = par + numero
        qtd_par = qtd_par + 1
    if numero % 2 == 1:
        impar = impar + numero
        qtd_impar = qtd_impar + 1
print(par, qtd_par, impar, qtd_impar)

#pratica 42 encotrar numeros acima e abaixo da media 
numeros = [12, 5, 18, 7, 20, 3, 10, 15]
soma = 0
acima_media = 0
abaixo_media = 0
soma_media = 0
soma_abaixo = 0
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
for numero in numeros:
    if numero > media:
        acima_media = acima_media + 1
        soma_media = soma_media + numero
    if numero < media:
        abaixo_media = abaixo_media + 1
        soma_abaixo = soma_abaixo + numero
print(media, acima_media, abaixo_media, soma_media, soma_abaixo)

#pratica 43 maior e menor acima da media 
numeros = [10, 5, 18, 7, 20, 3, 15, 12, 25, 8]
soma = 0 
maior_media = numeros[0]
p_maior = 0
menor_media = None
p_menor = 0
qtd = 0
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
for i in range(len(numeros)):
    if numeros[i] > media:
        qtd = qtd + 1
        if numeros[i] > maior_media:
            maior_media = numeros[i]
            p_maior = i
        if menor_media is None:
            menor_media = numeros[i]
            p_menor = i
        elif numeros[i] < menor_media:
            menor_media = numeros[i]
            p_menor = i
print(media, maior_media, p_maior, menor_media, p_menor, qtd)

#pratica 44 grupo filtado + none
numeros = [7, 22, 4, 18, 31, 9, 25, 12, 3]
maior_par = 0
p_par = 0
menor_par = None
m_par = 0
qtd = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        qtd = qtd +1
        if numeros[i] > maior_par:
            maior_par = numeros[i]
            p_par = i
        if menor_par is None:
            menor_par = numeros[i]
            m_par = i
        elif numeros[i] < menor_par:
            menor_par = numeros[i]
            m_par = i
print(maior_par, p_par, menor_par, m_par, qtd)

#pratica  45 maior e menor dos numeros impares
numeros = [16, 7, 21, 4, 13, 30, 9, 18, 5]
maior_impar = 0
p_maior = 0
menor_impar = None
p_menor = 0
qtd = 0 
soma = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 1:
        soma = soma + numeros[i]
        qtd = qtd + 1
        if numeros[i] > maior_impar:
            maior_impar = numeros[i]
            p_maior = i
        if menor_impar is None:
            menor_impar = numeros[i]
            p_menor = i
        elif numeros[i] < menor_impar:
            menor_impar = numeros[i]
            p_menor = i
print(maior_impar, p_maior, menor_impar,
      p_menor, soma, qtd)

#pratica 46 media dos pares
numeros = [8, 5, 12, 7, 20, 3, 14, 9, 6]
soma = 0
qtd = 0 
for numero in numeros:
    if numero % 2 == 0:
        soma = soma + numero
        qtd = qtd + 1
media = soma / qtd
print(soma, qtd, media)

#pratica 47 numeros acima da media 
numeros = [6, 14, 9, 21, 5, 18, 11, 25, 8]
soma = 0 
media = 0
qtd = 0
soma_acima = 0
maior_acima = None
p_media = None
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
for i in range(len(numeros)):
    if numeros[i] > media:
        soma_acima = soma_acima + numeros[i]
        qtd = qtd + 1
        if maior_acima is None:
            maior_acima = numeros[i]
            p_media = i
        elif numeros[i] > maior_acima:
            maior_acima = numeros[i]
            p_media = i
print(media, soma_acima, qtd, maior_acima, p_media)

#pratica 48 nivel acima 
numeros = [16, 7, 24, 9, 12, 31, 5, 18, 27, 10]
media = 0
qtd_acima = 0
soma = 0
soma_acima = 0
maior_media = None
p_maior = None
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
for i in range(len(numeros)):
    if numeros[i] > media:
        soma_acima = soma_acima + numeros[i]
        qtd_acima = qtd_acima + 1
        if maior_media is None:
            maior_media = numeros[i]
            p_maior = i
        elif numeros[i] > maior_media:
            maior_media = numeros[i]
            p_maior = i
print(media, qtd_acima, soma_acima, maior_media, p_maior)

#pratica 49  vamos subir um pouquinho 
numeros = [22, 7, 14, 31, 9, 18, 5, 26, 11, 20]
soma = 0
qtd = 0
abaixo_media = None
soma_abaixo = 0
menor_media = None
p_media = None
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
for i in range(len(numeros)):
    if numeros[i] < media:
        soma_abaixo = soma_abaixo + numeros[i]
        qtd = qtd + 1
        if menor_media is None:
            menor_media = numeros[i]
            p_media = i
        elif numeros[i] < menor_media:
            menor_media = numeros[i]
            p_media = i
print(media, qtd, soma_abaixo, menor_media, p_media)

#pratica 50 fechando um bloco importante 
numeros = [15, 8, 23, 4, 18, 31, 7, 12, 26, 9, 20]
soma = 0 
qtd_par = 0
soma_par = 0
maior_p = None
p_par = None
menor_p = None
p_menor = None
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        soma_par = soma_par + numeros[i]
        qtd_par = qtd_par + 1
        if maior_p is None:
            maior_p = numeros[i]
            p_par = i
        elif numeros[i] > maior_p:
            maior_p = numeros[i]
            p_par = i
        if menor_p is None:
            menor_p = numeros[i]
            p_menor = i
        elif numeros[i] < menor_p:
            menor_p = numeros[i]
            p_menor = i
print(media, qtd_par, soma_par, maior_p, p_par, menor_p, p_menor)

#pratica 51 agora quero ver adaptacao
numeros = [13, 4, 22, 17, 8, 29, 6, 15, 24, 11]
soma = 0
media = None
qtd_acima = 0
qtd_abaixo = 0
soma_acima = 0
soma_abaixo = 0
maior_abaixo = None
p_abaixo = None
for numero in numeros:
    soma = soma + numero
media = soma / len(numeros)
for i in range(len(numeros)):
    if numeros[i] > media:
        soma_acima = soma_acima + numeros[i]
        qtd_acima = qtd_acima + 1
    if numeros[i] < media:
        soma_abaixo = soma_abaixo + numeros[i]
        qtd_abaixo = qtd_abaixo + 1
        if maior_abaixo is None:
            maior_abaixo = numeros[i]
            p_abaixo = i
        elif numeros[i] > maior_abaixo:
            maior_abaixo = numeros[i]
            p_abaixo = i
print(media, qtd_acima, qtd_abaixo, soma_acima, soma_abaixo, maior_abaixo, p_abaixo)

#pratica 51 conceito : Dicionarios
aluno = {
    "nome": "Carlos",
    "idade": 20,
    "nota": 8.5
}
print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

#pratica 52
aluno = {
    "nome": "Carlos",
    "idade": 20,
    "nota": 8.5
}
aluno["idade"] = 21
aluno["nota"] = 9.0
print(aluno["idade"], aluno["nota"])
print(aluno)

#pratcia 53 adicionado uma informacao
aluno = {
    "nome": "Carlos",
    "idade": 21,
    "nota": 9.0
}
aluno["curso"] = "Python"
print(aluno)
#pratica 54
aluno = {
    "nome": "Carlos",
    "idade": 21,
    "nota": 9.0,
    "curso": "Python"
}
del aluno["idade"]
print(aluno)
#pratica 55 
aluno = {
    "nome": "Carlos",
    "idade": 20,
    "nota": 7.5
}
aluno["idade"] = 21
aluno["nota"] = 8.5
aluno["curso"] = "Python"
del aluno["idade"]
print(aluno)

#pratica 56
aluno = {
    "nome": "Ana",
    "idade": 22,
    "nota": 9.0,
    "curso": "Python"
}
for chave in aluno:
    print(chave, aluno[chave])

#pratica 57 agora vamos filtar
alunos = {
    "Ana": 8.5,
    "Carlos": 6.0,
    "João": 9.0,
    "Maria": 5.5
}
for chave in alunos:
    if alunos[chave] >= 7:
        print(chave, alunos[chave])

#pratica 58 dicionario + contador 
alunos = {
    "Ana": 8.5,
    "Carlos": 6.0,
    "João": 9.0,
    "Maria": 5.5,
    "Pedro": 7.5
}
soma = 0
qtd = 0
for chave in alunos:
    if alunos[chave] >= 7:
        qtd = qtd + 1
        soma = soma + alunos[chave]
media = soma / qtd
print(qtd, soma, media)

#pratica 59 dicionario filtro mais maior 
alunos = {
    "Ana": 7.5,
    "Carlos": 8.0,
    "João": 9.5,
    "Maria": 6.0,
    "Pedro": 8.5,
    "Lucas": 9.0 }
maior = 0
qtd = 0
soma = 0
nome = ""
for chave in alunos:
    if alunos[chave] >= 8:
        soma = soma + alunos[chave]
        qtd = qtd + 1
    if alunos[chave] > maior:
        maior = alunos[chave]
        nome = chave
print(maior, nome, qtd, soma)

#pratica 60 dicionarios + vrias informaçoes
alunos = {
    "Ana": 7.0,
    "Carlos": 5.5,
    "João": 9.0,
    "Maria": 8.5,
    "Pedro": 6.0,
    "Lucas": 10.0 }
media = None
qtd = 0
soma = 0
maior = 0
nome = ""
menor = 999
nome_m = ""
for chave in alunos:
    soma = soma + alunos[chave]
    if alunos[chave] >= 7:
        qtd = qtd + 1
    if alunos[chave] > maior:
        maior = alunos[chave]
        nome = chave
    if alunos[chave] < menor:
        menor = alunos[chave]
        nome_m = chave
media = soma / len(alunos)
print(media, qtd, soma, maior, nome, menor, nome_m)

#pratica 61 dicionario mais classificação
alunos = {
    "Ana": 8.5,
    "Carlos": 5.0,
    "João": 7.0,
    "Maria": 9.5,
    "Pedro": 6.5,
    "Lucas": 4.0 }
for chave in alunos:
    if alunos[chave] >= 7:
        print(chave, "Aprovado(a)")
    elif alunos[chave] >= 5 and alunos[chave] < 7:
        print(chave, "Recuperação")
    else:
        print(chave, "Reprovado")

#pratica 62 classificação + contagem
alunos = {
    "Ana": 8.5,
    "Carlos": 5.0,
    "João": 7.0,
    "Maria": 9.5,
    "Pedro": 6.5,
    "Lucas": 4.0 }
aprovados = 0
recuperacao = 0
reprovados = 0
for chave in alunos:
    if alunos[chave] >= 7:
        aprovados = aprovados + 1
    elif alunos[chave] >= 5:
        recuperacao = recuperacao + 1
    else:
        reprovados = reprovados + 1
print("Aprovados:",aprovados,"Recuperacao:", recuperacao, "Reprovados:", reprovados)

#pratica 63 dicionario + logica 
alunos = {
    "Ana": 8.5,
    "Carlos": 6.0,
    "João": 9.5,
    "Maria": 5.0,
    "Pedro": 7.0,
    "Lucas": 4.5}
aprovados = 0
recuperacao = 0
reprovados = 0
soma_a = 0
for chave in alunos:
    if alunos[chave] >= 7:
        aprovados = aprovados + 1
        soma_a = soma_a + alunos[chave]
    elif alunos[chave] >= 5:
        recuperacao = recuperacao + 1
    else:
        reprovados = reprovados + 1
media = soma_a / aprovados
print(aprovados, recuperacao, reprovados, soma_a, media)

#pratica dicionarios + logicas
produtos = {
    "Arroz": 25.0,
    "Feijão": 8.5,
    "Café": 18.0,
    "Leite": 6.0,
    "Açúcar": 5.5,
    "Macarrão": 7.0 }
qtd = 0
soma = 0
mais_c = 0
nome = None
menor = None
nome_m = None
for chave in produtos:
    if produtos[chave] > 10:
        qtd = qtd + 1
        soma = soma + produtos[chave]
    if produtos[chave] > mais_c:
        mais_c = produtos[chave]
        nome = chave
    if menor is None:
        menor = produtos[chave]
        nome_m = chave
    elif produtos[chave] < menor:
        menor = produtos[chave]
        nome_m = chave
print(qtd, soma, mais_c, nome, menor, nome_m)

#pratica 65 dicionario + logica 
vendas = {
    "Ana": 1200.0,
    "Carlos": 800.0,
    "João": 1500.0,
    "Maria": 600.0,
    "Pedro": 1100.0,
    "Lucas": 450.0 }
total = 0
media = 0
acima_media = 0
maior = None
nome = None
menor = None
nome_m = None
soma_a = 0
for chave in vendas:
    total = total + vendas[chave]
media = total / len(vendas)
for chave in vendas:
    if vendas[chave] > media:
        soma_a = soma_a + vendas[chave]
        acima_media = acima_media + 1
    if maior is None:
        maior = vendas[chave]
        nome = chave
    elif vendas[chave] > maior:
        maior = vendas[chave]
        nome = chave
    if menor is None:
        menor = vendas[chave]
        nome_m = chave
    elif vendas[chave] < menor:
        menor = vendas[chave]
        nome_m = chave
print(total, media, acima_media, maior, nome, menor, nome_m, soma_a)