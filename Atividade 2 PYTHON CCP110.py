# 1) Leia 2 valores e armazene-os nas variáveis A e B.
#  Efetue a soma de A e B e imprima o resultado na tela.

# A = int(input("Digite o valor de A: "))
# B = int(input("Digite o valor de B: "))
# soma = A + B
# print(soma)

# 2) Considerando a, b, c e d como variáveis com valores iniciais iguais a 5, 7, 3 e 9,
#  respectivamente, assinale a opção correta.

# 3) Uma granja classifica os ovos produzidos em pequeno e grande antes de embalá-los.
# Faça um programa que receba a medida dos ovos e os classifique seguindo a tabela a seguir:

# A = float(input("Digite a medida do ovo em mm: "))
# if A < 30:
#     print("pequeno")
# else:
#     print("grande")


# 4) Uma loja dá desconto de 10% para compras à vista, 5% para compras em 2 ou 3 parcelas e não dá desconto 
# compras acima de 3 parcelas. Além disso, a loja dá mais 5% de desconto (você pode somar essa porcentagem ao
# outro possível desconto) aos clientes que comprarem um total superior a R$5.000,00.
# Faça um programa para ler o valor da compra e o número de parcelas, calcular e mostrar o valor do desconto, 
# o valor final da compra com desconto e o valor de cada parcela. Utilize duas casas decimais.

# valor_compra = float(input("Digite o valor da compra: "))
# parcela = int(input("Digite a quantidade de parcelas: "))


# if parcela == 1:  
#     desconto = 0.10  # 10% à vista
# elif parcela == 2 or parcela == 3:  
#     desconto = 0.05   
# else:
#     desconto = 0.0    


# if valor_compra > 5000:
#     desconto += 0.05


# valor_desconto = valor_compra * desconto
# valor_final = valor_compra - valor_desconto
# valor_parcela = valor_final / parcela if parcela > 0 else valor_final


# print(f"Desconto total: {valor_desconto:.2f}")
# print(f"Valor final da compra com desconto: {valor_final:.2f}")
# print(f"Cada parcela será de: {valor_parcela:.2f}")

# Exercicio 5

# for i in range(5):
#     if i == 4:
#         continue
#     else:
#         print(i, end=" ")
# else:
#     print("Aqui", end=" ")

# Exercicio 6

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)

# Exercicio 7
# Escreva um programa que leia um valor inteiro n, onde n
#  é a quantidade de linhas de saída que serão apresentadas na execução do programa.
# A saída do programa deve ser feita seguindo o padrão dos exemplos fornecidos.

# Input:3
# Resultado
# Digite a quantidade de linhas: 3
# 1 1 1
# 2 4 8
# 3 9 27

# linhas = int(input("Digite o número de linhas: "))
# for i in range(1, linhas + 1):
#     print(i, i**2, i**3)

# Exercicio 8
# Escreva um programa que leia um valor inteiro
# n
# , onde
# n
# é a quantidade de linhas de saída que serão apresentadas na execução do programa.

# A saída do programa deve ser feita seguindo o padrão dos exemplos fornecidos.

# Input
# 3
# 8
# Resultado
# Digite a quantidade de linhas: 3
# 1 2 3 PIM
# 5 6 7 PIM
# 9 10 11 PIM

# Digite a quantidade de linhas: 8
# 1 2 3 PIM
# 5 6 7 PIM
# 9 10 11 PIM
# 13 14 15 PIM
# 17 18 19 PIM
# 21 22 23 PIM
# 25 26 27 PIM
# 29 30 31 PIM

# linhas = int(input("Digite a quantidade de linhas: "))
# contador = 1
# for i in range(linhas):
#     print(contador, contador + 1, contador + 2, "PIM")
#     contador += 4