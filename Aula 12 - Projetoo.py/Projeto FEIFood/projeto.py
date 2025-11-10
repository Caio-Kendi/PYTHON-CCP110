import os

# ==========================
# ARQUIVOS E CAMINHOS
# ==========================
CAMINHO_USUARIOS = "usuarios.txt"
CAMINHO_ALIMENTOS = "alimentos.txt"
CAMINHO_PEDIDOS = "pedidos.txt"

# ==========================
# FUNÇÕES DE USUÁRIO
# ==========================
def cadastrar_usuario():
    os.makedirs(".", exist_ok=True)
    nome = input("Nome completo: ")
    login = input("Escolha um login: ")
    senha = input("Escolha uma senha: ")

    if os.path.exists(CAMINHO_USUARIOS):
        with open(CAMINHO_USUARIOS, "r") as arq:
            for linha in arq:
                _, login_existente, _ = linha.strip().split(",")
                if login == login_existente:
                    print("❌ Esse login já existe. Tente outro.")
                    return

    with open(CAMINHO_USUARIOS, "a") as arq:
        arq.write(f"{nome},{login},{senha}\n")
    print("✅ Usuário cadastrado com sucesso!")


def login_usuario():
    if not os.path.exists(CAMINHO_USUARIOS):
        print("Nenhum usuário cadastrado ainda.")
        return None

    login = input("Login: ")
    senha = input("Senha: ")

    with open(CAMINHO_USUARIOS, "r") as arq:
        for linha in arq:
            nome, login_salvo, senha_salva = linha.strip().split(",")
            if login == login_salvo and senha == senha_salva:
                print(f"✅ Login realizado! Bem-vindo, {nome}.")
                return nome
    print("❌ Login ou senha incorretos.")
    return None

# ==========================
# FUNÇÕES DE ALIMENTOS
# ==========================
def inicializar_alimentos():
    if not os.path.exists(CAMINHO_ALIMENTOS):
        with open(CAMINHO_ALIMENTOS, "w") as arq:
            arq.write("Hamburguer,25.00\n")
            arq.write("Pizza,45.00\n")
            arq.write("Refrigerante,8.00\n")
            arq.write("Batata Frita,12.00\n")
            arq.write("Açaí,18.00\n")

def listar_alimentos():
    inicializar_alimentos()
    print("\n=== Lista de Alimentos ===")
    with open(CAMINHO_ALIMENTOS, "r") as arq:
        for linha in arq:
            nome, preco = linha.strip().split(",")
            print(f"- {nome}: R$ {preco}")

def buscar_alimento():
    inicializar_alimentos()
    termo = input("Digite o nome do alimento que deseja buscar: ").lower()
    encontrado = False
    with open(CAMINHO_ALIMENTOS, "r") as arq:
        for linha in arq:
            nome, preco = linha.strip().split(",")
            if termo in nome.lower():
                print(f"🍴 {nome} - R$ {preco}")
                encontrado = True
    if not encontrado:
        print("❌ Nenhum alimento encontrado com esse nome.")

# ==========================
# FUNÇÕES DE PEDIDOS
# ==========================
def criar_pedido(usuario):
    listar_alimentos()
    pedido = []
    while True:
        item = input("Digite o nome do alimento para adicionar (ou 0 para finalizar): ")
        if item == "0":
            break
        pedido.append(item)
    if not pedido:
        print("Nenhum item adicionado.")
        return
    with open(CAMINHO_PEDIDOS, "a") as arq:
        arq.write(f"{usuario}:{'|'.join(pedido)}:0\n")  # 0 = sem avaliação ainda
    print("✅ Pedido criado com sucesso!")

def listar_pedidos(usuario):
    if not os.path.exists(CAMINHO_PEDIDOS):
        print("Nenhum pedido encontrado.")
        return
    print("\n=== Seus Pedidos ===")
    with open(CAMINHO_PEDIDOS, "r") as arq:
        encontrados = False
        for linha in arq:
            nome, itens, nota = linha.strip().split(":")
            if nome == usuario:
                encontrados = True
                print(f"🧾 Itens: {itens.replace('|', ', ')} | Avaliação: {nota}")
        if not encontrados:
            print("Você ainda não tem pedidos.")

def excluir_pedido(usuario):
    if not os.path.exists(CAMINHO_PEDIDOS):
        print("Nenhum pedido encontrado.")
        return
    pedidos_novos = []
    encontrado = False
    with open(CAMINHO_PEDIDOS, "r") as arq:
        for linha in arq:
            nome, itens, nota = linha.strip().split(":")
            if nome == usuario:
                encontrado = True
                print(f"🗑️ Pedido removido: {itens.replace('|', ', ')}")
            else:
                pedidos_novos.append(linha)
    with open(CAMINHO_PEDIDOS, "w") as arq:
        arq.writelines(pedidos_novos)
    if not encontrado:
        print("Nenhum pedido para excluir.")
    else:
        print("✅ Pedido excluído com sucesso!")

def avaliar_pedido(usuario):
    if not os.path.exists(CAMINHO_PEDIDOS):
        print("Nenhum pedido encontrado.")
        return
    pedidos = []
    with open(CAMINHO_PEDIDOS, "r") as arq:
        pedidos = arq.readlines()
    with open(CAMINHO_PEDIDOS, "w") as arq:
        for linha in pedidos:
            nome, itens, nota = linha.strip().split(":")
            if nome == usuario and nota == "0":
                print(f"Pedido: {itens.replace('|', ', ')}")
                nova_nota = input("Dê uma nota de 0 a 5: ")
                arq.write(f"{nome}:{itens}:{nova_nota}\n")
                print("⭐ Avaliação registrada com sucesso!")
            else:
                arq.write(linha)

# ==========================
# MENUS PRINCIPAIS
# ==========================
def exibir_menu():
    print("\n=== FEIFood ===")
    print("1 - Cadastrar novo usuário")
    print("2 - Fazer login")
    print("0 - Sair")

def exibir_menu_usuario(nome):
    print(f"\n=== Bem-vindo, {nome}! ===")
    print("1 - Buscar alimento")
    print("2 - Listar todos os alimentos")
    print("3 - Criar pedido")
    print("4 - Listar meus pedidos")
    print("5 - Excluir pedido")
    print("6 - Avaliar pedido")
    print("0 - Logout")

# ==========================
# LOOP PRINCIPAL
# ==========================
def main():
    usuario_logado = None
    while True:
        if not usuario_logado:
            exibir_menu()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                cadastrar_usuario()
            elif opcao == "2":
                usuario_logado = login_usuario()
            elif opcao == "0":
                print("Saindo do sistema... Até logo!")
                break
            else:
                print("Opção inválida.")
        else:
            exibir_menu_usuario(usuario_logado)
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                buscar_alimento()
            elif opcao == "2":
                listar_alimentos()
            elif opcao == "3":
                criar_pedido(usuario_logado)
            elif opcao == "4":
                listar_pedidos(usuario_logado)
            elif opcao == "5":
                excluir_pedido(usuario_logado)
            elif opcao == "6":
                avaliar_pedido(usuario_logado)
            elif opcao == "0":
                usuario_logado = None
                print("Logout realizado com sucesso!")
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main()
