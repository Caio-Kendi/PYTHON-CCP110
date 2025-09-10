# Exercicio 1 - Laboratório 4

# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível,
# segundo o esquema abaixo, da esquerda para a direita.  Em seguida, conclua qual 
# dos animais seguintes foi escolhido, através das três palavras fornecidas. 
# Obs.: Não utilize acentuação no código.

# input_1 = input("Primeira palavra: ")
# input_2 = input("Segunda palavra: ")
# input_3 = input("Terceira palavra: ")
# if input_1 == ("invertebrado") and input_2 == "inseto" and input_3 == "hematofago":
#     print("pulga")

# if input_1 == "invertebrado" and input_2 == "inseto" and input_3 == "herbivoro":
#     print("lagarta")

# if input_1 == "invertebrado" and input_2 == "anelideo" and input_3 == "hematofago":
#     print("sanguessuga")

# if input_1 == "invertebrado" and input_2 == "anelideo" and input_3 == "onivoro":
#     print("minhoca")

# if input_1 == "vertebrado" and input_2 == "mamifero" and input_3 == "herbivoro":
#     print("vaca")

# if input_1 == "vertebrado" and input_2 == "mamifero" and input_3 == "onivoro":
#     print("homem")

# if input_1 == "vertebrado" and input_2 == "ave" and input_3 == "carnivoro":
#     print("aguia")

# if input_1 == "vertebrado" and input_2 == "ave" and input_3 == "onivoro":
#     print("pomba")
    

# ========================================================================================

# Exercicio 2 - Laboratorio 4

# Escreva um programa que determine o nome de uma forma a partir de seu número de lados.
# Leia o número de lados do usuário e relate o nome apropriado como parte de uma mensagem significativa.
# Seu programa deve oferecer suporte a formas de 3 a (incluindo) 10 lados.
# Se um número de lados fora desse intervalo for inserido, seu programa deverá exibir uma mensagem de erro.

# lados = int(input(""))

# if lados < 3:
#     print("Erro!")

# if lados > 10:
#     print("Erro!")

# if lados == 3:
#     print("triângulo")
    
# if lados == 4:
#     print("quadrado")

# if lados == 5:
#     print("pentágono")

# if lados == 6:
#     print("hexágono")

# if lados == 7:
#     print("heptágono")

# ============================================================

# Exercicio 3 - Laboratorio 4

# Faça um programa para exibir a idade de uma pessoa tendo como entrada a sua faixa etária, de acordo com a tabela abaixo: 

# Faixa etária	Idade
# Bebê	menor que 2 anos
# Criança	de 3 a 10 anos
# Adolescente	de 11 a 17 anos
# Adulto	de 18 a 64 anos
# Idoso	maior que 65 anos

# faixa_etaria = input("Digite a faixa etária: ")
# if faixa_etaria == "Bebê":
#     print("menor que 2 anos")

# if faixa_etaria == "Criança":
#     print("de 3 a 10 anos")

# if faixa_etaria == "Adolescente":
#     print("de 11 a 17 anos")

# if faixa_etaria == "Adulto":
#     print("de 18 a 64 anos")

# if faixa_etaria == "Idoso":
#     print("maior que 65 anos")

# ==================================================================

# Exercicio 4 - Laboratorio 4

# Uma loja dá desconto de 10% para compras à vista, 5% para compras em 2 ou 3 parcelas e não dá desconto para compras acima de 3 parcelas.
# Além disso, a loja dá mais 5% de desconto (você pode somar essa porcentagem ao outro possível desconto) aos clientes que comprarem
# um total superior a R$5.000,00. Faça um programa para ler o valor da compra e o número de parcelas, calcular e mostrar o valor
# do desconto,  o valor final da compra com desconto e o valor de cada parcela. Utilize duas casas decimais.

valor_compra = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))


if parcelas <= 1:
    valor_desconto = valor_compra * 0.10
    print(f"Desconto total: {valor_desconto}")
    valor_final = (valor_compra) - (valor_desconto)
    valor_final_parcelado = valor_final / parcelas  
    print(f"Valor final da compra com desconto: {valor_final:.2f} ")
    print(f"Cada parcela será de: {valor_final_parcelado:.2f} ")
    

elif parcelas == 2 or parcelas == 3:
    valor_desconto = valor_compra * 0.05
    print(f"Desconto total: {valor_desconto}")
    valor_final = (valor_compra) - (valor_desconto)
    valor_final_parcelado = valor_final / parcelas
    print(f"Valor final da compra com desconto: {valor_final:.2f} ")
    print(f"Cada parcela será de: {valor_final_parcelado:.2f} ")


elif valor_compra > 5000.00:
    valor_desconto = valor_compra * 0.05
    print(f"Desconto total: {valor_desconto}")
    valor_final = (valor_compra) - (valor_desconto)
    valor_final_parcelado = valor_final / parcelas
    print(f"Valor final da compra com desconto: {valor_final:.2f} ")
    print(f"Cada parcela será de: {valor_final_parcelado:.2f} ")





