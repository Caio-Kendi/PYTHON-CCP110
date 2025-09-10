# Desenvolva um algoritmo que pergunte ao usuário se ele deseja calcular o volume do Dodecaedro (12 faces) ou do Icosaedro (20 faces) regular. 
# Para realizar o cálculo, receba do usuário o valor da aresta a.

forma = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
valor_aresta = float(input("Digite o valor da aresta a em metros: "))
formula_dodecaedro = (15 + 7 * (5 ** 0.5)) / 4 * (valor_aresta ** 3)
formula_icosaedro = (5 * (3 + (5 ** 0.5))) / 12 * (valor_aresta ** 3)
if forma == "dodecaedro":
    print(f"O volume de um dodecaedro regular com {valor_aresta:.2f} de aresta é: {formula_dodecaedro:.2f}")
elif forma == "icosaedro":
    print(f"O volume de um icosaedro regular com {valor_aresta:.2f} de aresta é: {formula_icosaedro:.2f}")
