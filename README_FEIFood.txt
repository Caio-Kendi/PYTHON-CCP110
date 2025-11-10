FEIFood - README
=================

Descrição
---------
FEIFood é um sistema simples de pedidos de comida inspirado em plataformas como iFood. 
Este projeto foi desenvolvido em Python e utiliza arquivos de texto (.txt) para persistência de dados.
Versão entregue: implementação em um único arquivo (feifood.py) e relatório em formato .docx.

Conteúdo do repositório
-----------------------
- feifood.py          -> Código-fonte principal (versão em um único arquivo)
- usuarios.txt        -> Arquivo de dados de usuários (criado automaticamente)
- alimentos.txt       -> Arquivo de dados de alimentos (criado automaticamente)
- pedidos.txt         -> Arquivo de dados de pedidos e avaliações (criado automaticamente)
- Relatorio_FEIFood_Caio_Nakashima.docx -> Relatório final do projeto
- README.txt          -> Este arquivo (instruções e informações rápidas)

Requisitos
----------
- Python 3.8+ instalado
- Não há dependências externas (bibliotecas), apenas a biblioteca padrão do Python.

Como executar
-------------
1. Abra um terminal (cmd, PowerShell, bash, etc.).
2. Navegue até a pasta que contém o arquivo `feifood.py`.
3. Execute o comando:
   python feifood.py
4. Siga as instruções no menu textual exibido no terminal.

Funcionalidades implementadas
-----------------------------
- Cadastro de usuário (nome, login, senha) com verificação de login duplicado.
- Login de usuário (autenticação por login e senha).
- Inicialização automática de uma lista básica de alimentos na primeira execução.
- Busca por alimentos por termo (case-insensitive).
- Listagem de todos os alimentos disponíveis.
- Criação de pedidos (adicionar múltiplos itens por nome).
- Listagem dos pedidos realizados pelo usuário (com avaliação, se existir).
- Exclusão de pedidos do usuário.
- Avaliação de pedidos (nota de 0 a 5) e persistência dessa avaliação no arquivo de pedidos.

Formato dos arquivos
--------------------
- usuarios.txt: cada linha -> nome,login,senha
  Exemplo: Joao Silva,joaos,senha123

- alimentos.txt: cada linha -> nome,preco
  Exemplo: Pizza,45.00

- pedidos.txt: cada linha -> usuario:alimento1|alimento2|...:avaliacao
  Exemplo: Joao Silva:Pizza|Refrigerante:5

Observações e melhorias possíveis
--------------------------------
- Hoje as buscas por alimentos são feitas por nome exato/substring; poderia ser feita uma interface para selecionar por índice.
- Não há edição de pedidos (além de excluir e criar novamente); adicionar a edição seria um aprimoramento natural.
- Senhas são armazenadas em texto puro (simples para o escopo do exercício). Para produção, usar hashing (bcrypt) seria necessário.
- Poder adicionar funcionalidades de administrador (cadastrar/excluir alimentos, estatísticas) caso opte por versão em dupla/módulos.

Contato
-------
Desenvolvedor: Caio Nakashima
Email: caio.nakashima53@gmail.com (se quiser incluir)

Licença
-------
Projeto criado como parte das atividades da disciplina CCP110 - Fundamentos de Algoritmos (FEI).
