# Exercicio
# Crie 3 listas:
# ▶ Inteiros: a primeira lista com 10 números inteiros gerados
# aleatoriamente
# ▶ Reais: a segunda lista com 5 números reais gerados
# aleatoriamente
# ▶ Strings: A terceira lista com 7 strings criadas por você.
# Então adicione as 3 listas a uma lista única, chamada
# completa.
# Apague todas as 3 listas originais.
# Acesse e mostre todos os elementos da lista completa.
# Use:
# from random import randint, random
# print(randint(0, 10))
# print(random() * 10)

#Execução:

# from random import randint, random

# lista_int = [randint(1,100) for i in range(10)]

# lista_reais = [random () * 100 for i in range(5)]

# lista_strings = ["a","b","c","d","e","f","g","h","i","j"]

# completa = [lista_int[:],lista_reais[:],lista_strings[:]]
# print(completa)

# print("-----------------------------------------------")

# del lista_int
# del lista_reais
# del lista_strings

# print(completa)

#======================================================================

# A = [[1,2,3],[4,5,6],[7,8,9]]
# print(A)
# print(A[2])
# print(A[1][2])

# for linha in range(len(A)):
#     for coluna in range(len(A[linha])):
#         print(A[linha][coluna], end=" ")
#     print()

m = []

for num_linha in range(10):
    linha =[]
    for num_coluna in range(15):
        linha.append(num_linha + num_coluna)
    m.append(linha)

#ou

# m = [[num_linha + num_coluna for num_coluna in range(15)] for num_linha in range(10)]

for linha_matriz in range(len(m)): #printando em forma de matriz
    for coluna_matriz in range(len(m[linha_matriz])):
        print(f"{m[linha_matriz][coluna_matriz]:02}", end= " ")
    print()