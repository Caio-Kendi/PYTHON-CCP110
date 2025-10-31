# Exercicio 4 - Projeto

# Crie uma agenda de telefones que salva os dados de maneira
# permanente.
# A agenda deve funcionar em loop infinito, até que o usuário
# decida sair. Os dados armazenados são: nome, sobrenome,
# telefone e e-mail.
# A agenda deve apresentar o seguinte menu para o usuário:
# ▶ 1 - Novo contato (create)
# ▶ 2 - Procura (pelo nome) (read)
# ▶ 3 - Atualiza contato (update)
# ▶ 4 - Apaga contato (delete)
# ▶ 0 - Sair

0

menu = {
    "1": "Novo contato",
    "2": "Buscar contato",
    "3": "Atualiza contato",
    "4": "Apaga contato",
    "0": "Sair"
}

def exibir_menu():
    print("\nMenu da Agenda:")
    for chave, valor in menu.items():
        print(f"{chave} - {valor}")
    print()

def novo_contato():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    with open("contatos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{sobrenome},{telefone},{email}\n")
    print("Contato adicionado com sucesso!")
    print()
    
def buscar_contato():
    nome_busca = input("Digite o nome do contato que deseja buscar: ")
    encontrado = False
    with open("contatos.txt", "r") as arquivo:
        for linha in arquivo:
            nome, sobrenome, telefone, email = linha.strip().split(",")
            if nome.lower() == nome_busca.lower():
                print(f"Contato encontrado: {nome} {sobrenome}, Telefone: {telefone}, E-mail: {email}")
                encontrado = True
                break
    if not encontrado:
        print("Contato não encontrado.")

def atualizar_contato():
    nome_busca = input("Digite o nome do contato que deseja atualizar: ")
    linhas = []
    atualizado = False
    with open("contatos.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("contatos.txt", "w") as arquivo:
        for linha in linhas:
            nome, sobrenome, telefone, email = linha.strip().split(",")
            if nome.lower() == nome_busca.lower():
                print("Contato encontrado. Digite os novos dados:")
                novo_nome = input("Digite o novo nome: ")
                novo_sobrenome = input("Digite o novo sobrenome: ")
                novo_telefone = input("Digite o novo telefone: ")
                novo_email = input("Digite o novo e-mail: ")
                arquivo.write(f"{nome},{sobrenome},{novo_telefone},{novo_email}\n")
                atualizado = True
                print("Contato atualizado com sucesso!")
            else:
                arquivo.write(linha)

def apagar_contato():
    nome_busca = input("Digite o nome do contato que deseja apagar: ")
    linhas = []
    apagado = False
    with open("contatos.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("contatos.txt", "w") as arquivo:
        for linha in linhas:
            nome, sobrenome, telefone, email = linha.strip().split(",")
            if nome.lower() == nome_busca.lower():
                print(f"Contato apagado: {nome} {sobrenome}, Telefone: {telefone}, E-mail: {email}")
                apagado = True
            else:
                arquivo.write(linha)
    if apagado:              
                print("Contato apagado com sucesso!")
    else:
        print("Contato não encontrado.")
    print()
            

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo do programa. Até logo!")
        break
    if opcao == "1":
        novo_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        atualizar_contato()
    elif opcao == "4":
        apagar_contato()
    else:
        print("Opção inválida. Tente novamente.")