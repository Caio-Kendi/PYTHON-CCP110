# Exercício 1

# Escreva uma função chamada procuraChave que encontre todas as
# chaves, em um dicionário, que estão associadas a um valor
# específico.
# A função receberá o dicionário e o valor a procurar como seus
# únicos parâmetros.
# A função retornará uma lista (possivelmente vazia) de chaves
# associadas ao valor fornecido.
# Faça um programa principal que mostra o funcionamento da
# função.
# Seu programa principal deve criar um dicionário e mostrar que
# a função procuraChave funciona corretamente quando retorna
# várias chaves, uma única chave ou nenhuma chave.


# def procuraChave(dicionario, valorProcurado):
#     lista = []
#     for chave, valor in dicionario.items():
#         if valor == valorProcurado:
#             lista.append(chave)
#     return lista

# dicionario = {
#     'alfa': 1,
#     'bravo': 2,
#     'charlie': 3,
#     'delta': 4,
#     'echo': 5,
# }

# print(procuraChave(dicionario, 3))

# Deve mostrar: ['charlie']

#================================================================

# Exercício 2

# Faça um programa que gere 100 números aleatórios
# Gere números no intervalo de 0 à 20
# Mostre quantas vezes cada número apareceu
# Dica:
# Utilize um dicionário para armazenar o número como chave
# e a quantidade de vezes em que ele aparece como valor

# from random import randint

# lista = []
# for i in range(100):
#     lista.append(randint(0, 20))

# print(lista)

# dicionario = {}
# for numero in lista:
#     if numero in lista:
#         if numero in dicionario:
#             dicionario[numero] = dicionario[numero] + 1
#         else:
#             dicionario[numero] = 1

# print(dicionario)

#================================================================

# Exercício 3

# Neste exercício, você simulará 1000 lançamentos de dois dados.
# Comece escrevendo uma função que simula o lançamento de um par
# de dados de seis lados cada.
# Sua função não deve aceitar nenhum parâmetro.
# Ela retornará a somatória obtida pelos dois dados.
# Escreva um programa principal que use sua função para simular
# 1000 lançamentos de dois dados.
# Como acontece em alguns programas, você deve contar o número
# de vezes que cada somatória acontece.
# Em seguida, a função principal deve exibir uma tabela que
# resume esses resultados.
# Mostre a frequência para cada resultado como uma porcentagem
# do número total de lançamentos.

# from random import randint

# def lancar_dados():
#     dado1 = randint(1, 6)
#     dado2 = randint(1, 6)
#     return dado1 + dado2

# lista = []
# for _ in range(100000):
#     lista.append(lancar_dados())

# print(lista)

# dicionario = {}
# for numero in lista:
#     if numero in lista:
#         if numero in dicionario:
#             dicionario[numero] = dicionario[numero] + 1
#         else:
#             dicionario[numero] = 1

# dicionario = dict(sorted(dicionario.items()))

# print()
# print(dicionario)

# print()
# for chave, valor in dicionario.items():
#     porcentagem = (valor / 100000) * 100
#     print(f'Somatória {chave}: {porcentagem:.2f}%')

#================================================================

# Exercício 4

# Crie uma função que retorna o número de caracteres únicos em
# uma string criada pelo usuário.
# Por exemplo:
# “Hello, World!” tem 10 caracteres únicos
# enquanto zzz tem somente 1 caractere único.
# Use um dicionário para resolver este problema.

# palavra = input('Digite uma palavra ou frase: ')

# dicionario = {}
# for letra in palavra:
#     if letra in dicionario:
#         dicionario[letra] += 1
#     else:
#         dicionario[letra] = 1

# print(dicionario)
# print(len(dicionario))

#================================================================

# Exercício 5

# Duas palavras são anagramas se contiverem todas as mesmas
# letras, mas em uma ordem diferente.
# Por exemplo: estante e setenta são anagramas.
# Crie uma função que recebe duas strings do usuário e determina
# se elas são ou não anagramas.
# Utilize dicionário para resolver o problema.

def eh_anagrama(palavra1, palavra2):
    dicionario1 = {}
    for letra in palavra1:
        if letra in dicionario1:
            dicionario1[letra] += 1
        else:
            dicionario1[letra] = 1

    dicionario2 = {}
    for letra in palavra2:
        if letra in dicionario2:
            dicionario2[letra] += 1
        else:
            dicionario2[letra] = 1

    return dicionario1 == dicionario2

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

print(eh_anagrama(palavra1, palavra2))
