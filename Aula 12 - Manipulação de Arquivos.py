# arquivo = open("teste.txt", "w")

# for linha in range(1, 101):
#     arquivo.write(f"Linha {linha}\n")

# arquivo.close()

# arquivo = open("teste.txt", "r")

# for linha in arquivo.readlines():
#     print(linha.strip())

# arquivo.close()


# pares = open("pares.txt", "w")
# impares = open("impares.txt", "w")

# for numero in range(0,1000):
#     if numero % 2 == 0:
#         pares.write(f"{numero}\n")
#     else:
#         impares.write(f"{numero}\n")

# pares.close()
# impares.close()

# ===============================================

# with open("pares.txt", "r") as pares, open("multiplos.txt", "w") as multiplos:
#     for linha in pares.readlines():
#         valor = int(linha.strip())
#         if valor % 4 == 0:
#             multiplos.write(linha)

# ================================================

# with open("contatos.txt", "a") as contatos:
#     while True:
#         nome = input("Digite o nome: ")
#         telefone = input("Digite o telefone: ")
#         if nome == "" or telefone == "":
#             break
#         contatos.write(f"{nome}, {telefone}\n")

# with open("contatos.txt", "r") as contatos:
#     print("-" * 45)
#     print(f"|{'Nome':>25} | {'Telefone':<15} |")
#     print("-" * 45)
#     for linha in contatos:
#         nome, telefone = linha.strip().split(", ")
#         print(f"| {nome:>25} | {telefone:<15}|")
#     print("-" * 45)

# ==================================================

# Exercicio 2

# Crie um arquivo: “numeros.txt” que contenha 100 números
# aleatórios;
# Todos os números do arquivo estão na mesma e única linha,
# separados por espaço;
# Escreva uma função em Python para retornar a somatória de
# todos os números que estão armazenados no arquivo
# “numeros.txt”.

# from random import randint

# with open("numeros.txt", "w") as numeros:
#     for _ in range(100):
#         numeros.write(f"{randint(1,1000)} ")

# def soma_arquivo(nome_arquivo):
#     with open(nome_arquivo, "r") as arquivo:
#         conteudo = arquivo.read()
#         print(f"Conteúdo do arquivo: {conteudo}")
#         numeros = conteudo.split()
#         print(f"Números encontrados: {numeros}")
#         soma = 0
#         for numero in numeros:
#             soma += int(numero)
#     return soma

# resultado = soma_arquivo("numeros.txt")
# print(f"A soma dos números no arquivo é: {resultado}")

# ==================================================

# Exercicio 3

# Crie um arquivo: “numeros.txt” que contenha 100 números
# aleatórios;
# Escreva uma função que leia uma sequência numérica do arquivo
# “numeros.txt” e salva os números na lista num.
# Escreva outra função que recebe a lista num como parâmetro e
# retorna uma nova lista num_unicos, sem os elementos repetidos.
# Escreva uma terceira função que recebe a lista num_unicos e
# grava os números no arquivo “numeros_unicos.txt”.

from random import randint

def gerar_numeros():
    with open("numeros.txt", "w") as numeros:
        for _ in range(100):
            numeros.write(f"{randint(1,1000)} ")

def ler_numeros():
    with open("numeros.txt", "r") as numeros:
        conteudo = numeros.read()

    num = []
    for numero in conteudo.strip().split():
        num.append(int(numero))
    return num

def remover_repetidos(lista):
    return list(set(lista))

def salvar_numeros_unicos(numeros_unicos):
    with open("numeros_unicos.txt", "w") as arquivo:
        for numero in numeros_unicos:
            arquivo.write(f"{numero}\n")

gerar_numeros()
numeros_lidos = ler_numeros()
print(f"Números lidos: {numeros_lidos}")
numeros_unicos = remover_repetidos(numeros_lidos)
print(f"Números únicos: {numeros_unicos}")
print(f"Numeros {len(numeros_lidos)} lidos, {len(numeros_unicos)} únicos.")
salvar_numeros_unicos(numeros_unicos)
