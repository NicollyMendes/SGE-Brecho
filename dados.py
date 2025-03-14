import sqlite3


conexao = sqlite3.connect('dados_brecho.db')

# Criar tabela de Itens 
conexao.execute('CREATE TABLE Itens(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                nome TEXT NOT NULL,\
                descricao TEXT,\
                tamanho TEXT,\
                cor TEXT,\
                preco REAL,\
                quantidade_em_estoque INTEGER)') 

# Criar tabela de Clientes 
conexao.execute('''
    CREATE TABLE Clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,  -- CPF único e obrigatório
        cep TEXT,
        endereco TEXT,
        complemento TEXT,
        uf TEXT,
        email TEXT,
        num_telefone TEXT
    )
''')

# Criar tabela de Vendas 
conexao.execute('CREATE TABLE Vendas(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                id_item INTEGER,\
                id_cliente INTEGER,\
                data_venda TEXT,\
                quantidade_vendida INTEGER,\
                FOREIGN KEY(id_item) REFERENCES Itens(id),\
                FOREIGN KEY(id_cliente) REFERENCES Clientes(id))')

# Salvar as alterações e fechar a conexão
conexao.commit()
conexao.close()
