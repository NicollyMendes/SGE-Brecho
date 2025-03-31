# Sistema de Gerenciamento de Estoque e Vendas para Brechó
Este é um sistema de gerenciamento de estoque e vendas desenvolvido em Python com uma interface gráfica (GUI)
utilizando Tkinter. O sistema foi projetado para ajudar brechós e pequenos negócios a organizar seus estoques,
realizar vendas, gerenciar clientes e visualizar informações importantes de maneira simplificada e acessível.

## Funcionalidades
  - **Cadastro de Clientes:** Permite cadastrar novos clientes com campos como nome, CPF (com validação), endereço, e-mail, telefone, entre outros.
  - **Cadastro de Produtos(Itens):** Possibilita o registro de itens no estoque, com detalhes como nome, descrição, tamanho, cor, preço e quantidade disponível.
  - **Controle de Estoque:** O sistema atualiza automaticamente a quantidade em estoque após cada venda e verifica a disponibilidade antes de confirmar uma venda.
  - **Realização de Vendas:** Permite realizar vendas, selecionando clientes e produtos, e gera um resumo da venda incluindo o valor total.
  - **Visualização de Vendas:** Mostra todas as vendas realizadas com informações sobre o cliente, item vendido, quantidade e valor total.
  - **Backup Semanal:** Cria cópias automáticas semanais do banco de dados para garantir a segurança das informações.

## Estrutura do Projeto
O Projeto é organizado em três módulos principais:
  - **tela.py:** Contém a interface gráfica e a interação com o usuário.
  - **dados.py:** Responsável pelo gerenciamento de dados no banco SQLite.
  - **view.py:** Inclui a loógica de controle e manipulação ds dados, como as funções para cadastrar clientes, produtos e vendas.

## Tecnologias Usadas
  - **Python 3.x:** Linguagem principal para o desenvolvimento do sistema.
  - **Tkinter:** Biblioteca para criar a interface gráfica do usuário.
  - **SQLite:** Banco de dados embutido, utilizado para armazenar informações sobre clientes, produtos e vendas.
  - **Shutil:** Biblioteca para realizar o backu automático semanal no banco de dados.

## Instalação
1. **Clone o repositório**
   ```bash
   git clone https://github.com/NicollyMendes/SGE-Brecho.git
2. **Acesse a pasta do projeto**
   ```bash
   cd SGE-Brecho
3. **Instale as dependências necessárias**
   ```bash
   pip install -r requeriments.txt
4. **Execute o projeto**
   ```bash
   python tela.py
**Nota**: Certifique-se de que a pasta dados exisa no diretório do projeto e contenha o banco de dados SQLite (dados_brecho.db)

## Como Usar
# Interface Principal
A interface principal contém uma barra de navegação lateral com as principais funcionalidades do sistema:
1. **Cadastrar Cliente**: Permite adicionar um novo cliente ao sistema.
2. **Cadastrar Item**: Permite adicionar um novo item ao estoque.
3. **Exibir Clientes**: Exibe uma lista de todos os clientes cadastrados.
4. **Exibir Itens**: Mostra todos os itens atualmente no estoque.
5. **Realizar Venda**: Permite registrar uma venda, selecionando o cliente e o item desejado
6. **Visualizar Vendas**: Exibe o histórico de todas as vendas realizadas.

# Backup Semanal
O sistema realiza automaticamente um backup semanal do banco de dados para garantir a integridade e segurança dos dados. A cópia do banco de dados é armazenada na pasta backup, no diretório do projeto.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

## Contato
Desenvolvido por Nicolly Mendes -
[nicollycescon22@gmail.com](mailto:nicollycescon22@gmail.com)
  
