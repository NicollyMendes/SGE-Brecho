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
def insert_cliente(nome, sobrenome, endereco, email, num_telefone):
    conexao = connect()
    conexao.execute("INSERT INTO Clientes(nome, sobrenome, endereco, email, num_telefone)\
                     VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, num_telefone))
    conexao.commit()
    conexao.close()

# Função para exibir os clientes
def get_clientes():
    conexao = connect()
    c = conexao.cursor()
    c.execute("SELECT id, nome, email, num_telefone FROM Clientes") 
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
    conexao.execute("INSERT INTO Vendas(id_item, id_cliente, data_venda, quantidade_vendida)\
                    VALUES(?, ?, ?, ?)", (id_item, id_cliente, data_venda, quantidade_vendida))
    conexao.commit()
    conexao.close()

# Função para exibir todos os itens vendidos
def get_itens_vendidos():
    conexao = connect()
    resultado = conexao.execute("SELECT Vendas.id, Itens.nome, Clientes.nome, Clientes.sobrenome, Vendas.data_venda, Vendas.quantidade_vendida\
                                FROM Itens\
                                INNER JOIN Vendas ON Itens.id = Vendas.id_item\
                                INNER JOIN Clientes ON Clientes.id = Vendas.id_cliente").fetchall() 
    conexao.close()
    return resultado

# Função para atualizar o estoque do item após uma venda
def update_item_estoque(id_item, quantidade_vendida):
    conexao = connect()
    conexao.execute("UPDATE Itens SET quantidade_em_estoque = quantidade_em_estoque - ? WHERE id = ?", (quantidade_vendida, id_item))
    conexao.commit()
    conexao.close()
