# EXERCICIO 1

# Faça um programa que imprima os números ímpares entre 0 e um
# número digitado pelo usuário

# COMANDO WHILE

# x = 0 
# n = int (input ("Digite um número positivo: ") )
# while x <= n:
#     if x % 2 != 0:
#         print (x)
#     x = x + 1






# EXERCICIO 2

# Faça um programa que imprima os números de 1 a 50 de 1 em 1 e
# de 52 a 100 de 2 em 2;

# COMANDO WHILE
# X = 1
# while X <= 50:
#     print (X)
#     X = X + 1

# X = 52
# while X <= 100:
#     print (X)
#     X = X + 2

# COMANDO FOR

# for X in range (1, 51):
#     print (X)

# for X in range (52, 101, 2):
#     print (X)

# ==================================================================================


# EXERCICIO 3

# Escreva um programa que imprima a tabuada de um número
# digitado pelo usuário;

# n = int (input ("Digite um número para ver a tabuada: ") )
# for X in range (1, 11):
#     resultado = n * X
#     print (f"{n} x {X} = {resultado}")

# ==================================================================================

# EXERCICIO 4

# Faça um programa que leia 6 números inteiro positivos do
# usuário exiba o maior o número lido;

# for X in range (6):
#     n = int (input ("Digite um número positivo: ") )
#     if X == 0:
#         maior = n
#     elif n > maior:
#         maior = n

# print ("O maior número digitado foi: ", maior)

# ==================================================================================

# EXERCICIO 5

# Faça um programa que solicita um número entre 0 e 10
# ▶ Mostre uma mensagem de erro caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
# ▶ Quando o valor for válido dê a mensagem “número aceito”.
# ▶ Dica: você pode utilizar operadores lógicos (and ou or) na
# condição do while também!


# while True:
#         n = int (input ("Digite um número entre 0 e 10: ") )
#         while n < 0 or n > 10:
#             break
#         print ("Número inválido, tente novamente!")
#         n = int (input ("Digite um número entre 0 e 10: ") )
#         if n >= 0 and n <= 10:
#             print ("Número aceito!")

# ==================================================================================

# EXERCICIO 6

#  Escreva um programa que leia números digitados pelo usuário
# ▶ O programa deve ler os números até que o 0 (zero) seja digitado.
# ▶ Quando o 0 for digitado, o programa deve exibir:
# ⋆ a quantidade de números que foram digitados;
# ⋆ a somatória destes números;
# ⋆ e a média aritmética.

# quantidade = 0
# somatoria = 0
# while True:
#     n = int (input ("Digite um número (0 para sair): ") )
#     if n == 0:
#         break
#     quantidade = quantidade + 1
#     somatoria = somatoria + n
# media = somatoria / quantidade
# print ("Quantidade de números digitados: ", quantidade)
# print ("Somatória dos números digitados: ", somatoria)
# print ("Média aritmética dos números digitados: ", media)


# ==================================================================================

# EXERCICIO 7

#  Faça um programa para calcular a somatória de 10 números
# ▶ Os número devem ser digitados pelo usuário
# ▶ Será necessário um contador para controlar o número de
# repetições
# ▶ e um acumulador para acumular a soma dos números entre cada
# repetição






