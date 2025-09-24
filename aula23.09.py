# Exercicio 1
# Crie uma função que calcule a média de dois números
# ▶ Sua função deve receber dois números como parâmetros de entrada
# ▶ Deve imprimir o resultado da média

# entrada1 = float(input("Digite o primeiro numero: "))
# entrada2 = float(input("Digite o segundo numero: "))

# def media (entrada1, entrada2):
#     res = (entrada1 + entrada2)/2
#     return res

# print(f"A média dos dois numeros é: {media(entrada1, entrada2):.2f}")

# Exercicio 2
# Adapte a função para calcular a média criada anteriormente.
# ▶ Faça com que ela retorne o resultado da média para o chamador da
# função.




# Exercicio 3
# Escreva uma função com parâmetros que retorne o maior de dois
# números.
# ▶ A função deve se chamar maximo(x, y)

# entrada1 = float(input("Digite o primeiro numero: "))
# entrada2 = float(input("Digite o segundo numero: "))

# def maximo(entrada1, entrada2):
#     if entrada1 > entrada2:
#         return entrada1
#     else:
#         return entrada2
    
# print(f"O maior numero é: {maximo(entrada1, entrada2):.2f}") 

# Exercicio 4
# Escreva uma função com parâmetros chamada multiplo(x, y).
# ▶ Esta função deve receber dois números
# ▶ Retornar True se o primeiro for múltiplo do segundo número;
# ▶ Retornar False caso contrário.

# entrada1 = int(input("Digite o primeiro numero inteiro: "))
# entrada2 = int(input("Digite o segundo numero inteiro: "))

# def multiplo(entrada1, entrada2):
#     if entrada1 % entrada2 == 0:
#         print("True")
#     else:
#         print("False")

# multiplo(entrada1, entrada2)

# Exercicio 5
# Escreva uma função com parâmetros que:
# ▶ Receba a base e a altura de um triângulo e retorne sua área

# base_triangulo = int(input("Digite a base do triangulo: "))
# altura_triangulo = int(input("Digite a altura do triangulo: "))

# def area_triangulo(base_triangulo, altura_triangulo):
#     res = (base_triangulo * altura_triangulo)/2
#     return res

# print(f"A area do triangulo é: {area_triangulo(base_triangulo, altura_triangulo)}")

# Exericio 6
# Faça um programa que:
# ▶ Leia três números e apresente o resultado do seguinte cálculo:
# √n1 + √n2 + √n3 + (n1 + n2)/2 + (n2 + n3)/2 + (n1 + n3)/2

# a = int(input("Digite o primeiro numero: "))
# b = int(input("Digite o segundo numero: "))
# c = int(input("Digite o terceiro numero: "))

# raiz_quadrada_a = a ** 0.5
# raiz_quadrada_b = b ** 0.5
# raiz_quadrada_c = c ** 0.5

# def calculo(a, b, c):
#     res = (raiz_quadrada_a + raiz_quadrada_b + raiz_quadrada_c + (a + b)/2 + (b + c)/2 + (a + c)/2)
#     return res

# print(f"O resultado do calculo das três entradas é: {calculo(a, b, c):.2f}")

# Exercicio 7 
# Existem restrições para que uma pessoa possa doar sangue. Uma
# delas é relativa ao peso. Mulheres tem que pesar no mínimo
# 50kg e homens no mínimo 60kg. Faça uma função para informar
# se uma pessoa está ou não apta a doar sangue sabendo seu sexo
# e seu peso.

# O programa principal deve ler as entradas, acionar a função e
# exibir a resposta.

# sexo = str(input("Digite o seu sexo(M/F): "))
# peso = float(input("Digite o seu peso: "))

# def calculo(sexo, peso):
#     if sexo.upper() == "M" and peso >= 60:
#         return "Apto para doar sangue"
#     elif sexo.upper() == "F" and peso >= 50:
#         return "Apta para doar sangue"
#     else:
#         return "Não está apto(a) para doar sangue"

# print(calculo(sexo, peso))