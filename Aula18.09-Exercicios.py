# Exercicio 1
# Faça um programa que receba uma série de números naturais e
# contabilize quantos desses números são primos. Lembre-se, um
# número x é primo se x > 1 e seus únicos divisores são 1 e o
# próprio x.


# n = int(input("Digite quantos numeros serão verificados: "))
# contador_primos = 0

# for i in range(n):
#     x = int(input("Digite um numero natural: "))
#     eh_primo = True
#     if x < 2:
#         eh_primo = False
#     else:
#         for j in range(2, x):
#             if x % j == 0 and x % x == 0:
#                 eh_primo = False
#             break


#     if eh_primo and x > 1:
#         contador_primos += 1
       
# print(f"A quantidade de numeros primos é: {contador_primos}")

# ==========================================================

# Exercicio 2
# Faça um programa que permita imprimir apenas as bordas de um
# retângulo. O programa recebe dois números inteiros L > 0 e
# C > 0 que representam o número de linhas e número de colunas do
# retângulo.

# num_linhas = int(input("Digite o numero de linhas: "))
# num_colunas = int(input("Digite o numero de colunas: "))

# for linha in range(num_linhas):
#     for coluna in range(num_colunas):
#         if linha == 0 or linha == num_linhas - 1 or coluna == 0 or coluna == num_colunas - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# ==========================================================

# Exercicio 3
# Faça um programa que permita imprimir uma representação de um
# tabuleiro quadrado de xadrez. e "0" entre as estrelas(*).

# num_colunas = int(input("Digite o numero de colunas: "))
# num_linhas = int(input("Digite o numero de linhas: "))
# for linha in range(num_linhas):
#     for coluna in range(num_colunas):
#         if (linha + coluna) % 2 == 0:
#             print("*", end="")
#         else:
#             print("0", end="")
#     print()

# ===========================================================

# Exercicio 4
# Faça um programa que permita imprimir uma representação de uma
# tabela quadrada com o seguinte padrão:
# 5
# @@@@@
# $@@@@
# $$@@@
# $$$@@
# $$$$@

num_colunas = int(input("Digite o numero de colunas: "))
num_linhas = int(input("Digite o numero de linhas: "))
for linha in range(num_linhas):
    for coluna in range(num_colunas):
         if linha < coluna:
             print("$", end = "_")
         else:
             print("@", end = "_")
    print()

# num_colunas = int(input("Digite o numero de colunas: "))
# num_linhas = int(input("Digite o numero de linhas: "))
# for linha in range(num_linhas):
#     for coluna in range(num_colunas):
#         if linha < coluna:
#             print("$", end = "")
#         else:
#             print("@", end = "")
#     print()





