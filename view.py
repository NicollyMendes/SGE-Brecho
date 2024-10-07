import sqlite3

# Conectar ao banco de dados
# Função criada para conexão ao banco
def connect():
    conexao = sqlite3.connect('dados_brecho.db')
    return conexao

# Função para inserir um novo item na tabela Itens
def insert_item(nome, descricao, tamanho, cor, preco, quantidade_em_estoque):
    conexao = connect()
    conexao.execute("INSERT INTO Itens(nome, descricao, tamanho, cor, preco, quantidade_em_estoque)\
                     VALUES (?, ?, ?, ?, ?, ?)", (nome, descricao, tamanho, cor, preco, quantidade_em_estoque))
    conexao.commit()
    conexao.close()

# Função para inserir clientes
def insert_cliente(nome, cpf, cep, endereco, complemento, uf, email, num_telefone):
    conexao = connect()
    cursor = conexao.cursor()

    # Inserir os dados no banco de dados
    cursor.execute('''
        INSERT INTO Clientes(nome, cpf, cep, endereco, complemento, uf, email, num_telefone)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, cpf, cep, endereco, complemento, uf, email, num_telefone))

    conexao.commit()
    conexao.close()
# Função para exibir os clientes
def get_clientes():
    conexao = connect()
    c = conexao.cursor()
    c.execute("SELECT id, nome, cpf, email, num_telefone FROM Clientes") 
    clientes = c.fetchall()
    conexao.close()
    return clientes 

# Função para exibir os itens do brechó
def get_itens():
    conexao = connect()
    itens = conexao.execute("SELECT * FROM Itens").fetchall()
    conexao.close()
    return itens

# Função para realizar uma venda
def insert_venda(id_cliente, id_item, data_venda, quantidade_vendida):
    conexao = connect()
    cursor = conexao.cursor()

    # Insere a venda no banco de dados
    cursor.execute("""
        INSERT INTO Vendas (id_item, id_cliente, data_venda, quantidade_vendida)
        VALUES (?, ?, ?, ?)
    """, (id_item, id_cliente, data_venda, quantidade_vendida))

    conexao.commit()
    conexao.close()



# Função para buscar as vendas realizadas
def get_itens_vendidos():
    conexao = connect()
    cursor = conexao.cursor()

    # Consulta SQL para buscar as informações da venda, incluindo o preço do item
    cursor.execute("""
        SELECT Vendas.id, Itens.nome, Clientes.nome, Vendas.data_venda, 
               Vendas.quantidade_vendida, Itens.preco
        FROM Vendas
        INNER JOIN Itens ON Vendas.id_item = Itens.id
        INNER JOIN Clientes ON Vendas.id_cliente = Clientes.id;
    """)

    resultado = cursor.fetchall()
    
    # Imprime os resultados para depuração
    print("Dados retornados pela consulta SQL:", resultado)

    conexao.close()
    return resultado





# Função para atualizar o estoque do item após uma venda
def update_item_estoque(id_item, quantidade_vendida):
    conexao = connect()
    conexao.execute("UPDATE Itens SET quantidade_em_estoque = quantidade_em_estoque - ? WHERE id = ?", (quantidade_vendida, id_item))
    conexao.commit()
    conexao.close()

def preencher_comboboxes(combo_cliente, combo_item):
    # Obter os clientes e itens cadastrados no banco de dados
    clientes = get_clientes()  # Esta função deve retornar algo como [(1, "João", "email", "telefone"), (2, "Maria", ...)]
    itens = get_itens()        # Esta função deve retornar algo como [(1, "Camiseta", "Descrição", "Tamanho", ...)]

    # Preencher a combobox de clientes
    clientes_formatados = [f"{cliente[0]} - {cliente[1]}" for cliente in clientes]  # Ex: "1 - João Silva"
    combo_cliente['values'] = clientes_formatados

    # Preencher a combobox de itens
    itens_formatados = [f"{item[0]} - {item[1]}" for item in itens]  # Ex: "1 - Camiseta Branca"
    combo_item['values'] = itens_formatados

