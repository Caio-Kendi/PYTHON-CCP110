
# a = int (input ("Lado a: ") )
# b = int (input ("Lado b: ") )
# c = int (input ("Lado c: ") )

# if (a < b + c) and (b < a + c) and (c < a + b):
#     print("os valores formam um triangulo")
#     if (a == b) and (b == c):
#         print("Triangulo equilatero")
#     elif (a == b) or (a == c) or (b == c):
#         print("Triangulo isosceles")
#     else:
#         print("Triangulo escaleno")
# else:
#     print("não é um triangulo")
# #fim

#=========================================================

# Exercicio 1 - Construa um algoritmo que, tendo como dados de entrada o preço
# de um produto e seu código de origem, mostre o preço junto de
# sua procedência. Caso o código não seja nenhum dos
# especificados, o produto deve ser encarado como importado.
# Siga a tabela de códigos:

# preco = float(input("Digite o preço do produto: "))
# codigo_produto = int(input("Digite o código do produto: "))

# if codigo_produto == 1:
#     print(preco)
#     print("procedencia: Sul")
# elif codigo_produto == 2:
#     print(preco)
#     print("procedencia: Norte")
# elif codigo_produto == 3:
#     print(preco)
#     print("procedencia: Leste")
# elif codigo_produto == 4:
#     print(preco)
#     print("procedencia: Oeste")
# elif codigo_produto == 5 or codigo_produto == 6:
#     print(preco)
#     print("procedencia: Nordeste")
# elif codigo_produto == 7 or codigo_produto == 8 or codigo_produto == 9:
#     print(preco)
#     print("procedencia: Sudeste")
# elif codigo_produto >= 10 and codigo_produto <= 20:
#     print(preco)
#     print("procedencia: Centro-Oeste")
# elif codigo_produto >= 21 and codigo_produto <= 30:
#     print(preco)
#     print("procedencia: Noroeste")
# else:
#     print("produto importado")

#=========================================================

# Exercicio 2 - 2. Escreva um algoritmo que leia três valores inteiros e
# diferentes e mostre-os em ordem decrescente.


# Primeiro_valor = int(input("Digite o primeiro valor: "))
# Segundo_valor = int(input("Digite o segundo valor: "))
# Terceiro_valor = int(input("Digite o terceiro valor: "))

# if (Primeiro_valor > Segundo_valor) and (Primeiro_valor > Terceiro_valor) and (Segundo_valor > Terceiro_valor):
#     print(Primeiro_valor)
#     print(Segundo_valor)
#     print(Terceiro_valor)
# elif(Primeiro_valor > Segundo_valor) and (Primeiro_valor > Terceiro_valor) and (Terceiro_valor > Segundo_valor):
#     print(Primeiro_valor)
#     print(Terceiro_valor)
#     print(Segundo_valor)
# elif (Segundo_valor > Primeiro_valor) and (Segundo_valor > Terceiro_valor) and (Primeiro_valor > Terceiro_valor):
#     print(Segundo_valor)
#     print(Primeiro_valor)
#     print(Terceiro_valor)
# elif (Segundo_valor > Primeiro_valor) and (Segundo_valor > Terceiro_valor) and (Terceiro_valor > Primeiro_valor):
#     print(Segundo_valor)
#     print(Terceiro_valor)
#     print(Primeiro_valor)
# elif (Terceiro_valor > Primeiro_valor) and (Terceiro_valor > Segundo_valor) and (Primeiro_valor > Segundo_valor):
#     print(Terceiro_valor)
#     print(Primeiro_valor)
#     print(Segundo_valor)
# elif (Terceiro_valor > Primeiro_valor) and (Terceiro_valor > Segundo_valor) and (Segundo_valor > Primeiro_valor):
#     print(Terceiro_valor)
#     print(Segundo_valor)
#     print(Primeiro_valor)

#=========================================================

# Exercicio 3 - Tendo como dados de entrada a altura e o sexo de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando
# as seguintes fórmulas:
# ▶ para homens: (72,7 * h) - 58;
# ▶ para mulheres: (62,1 * h) - 44,7.

# sexo = input("Digite o seu sexo (M/F): ")
# altura = float(input("Digite a sua altura: "))

# if sexo == "M":
#     print("seu peso ideal é de: ", (72.7 * altura) - 58)
# elif sexo == "F":
#     print("seu peso ideal é de: ", (62.1 * altura) - 44.7)
