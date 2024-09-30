#CRIACAO DA INTERFACE GRÁFICA
from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from  tkinter import messagebox
from datetime import date
from datetime import datetime

# importando as funções da view
from view import *

hoje = date.today()

# CORES
co0 = "#2e2d2b" #Preta
co1 = "#feffff" #Branca ------ padrão 
co2 = "#4fa882" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra
co5 = "#e06636" # - profit
co6 = "#E9A178"
co7 = "#3fbfb9" #Verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde
co10 = "#6e8faf"
co11 = "#f2f4f2"

#Criando janela  ------
janela = Tk()
janela.title('')
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

#Frames ------
frameCima = Frame(janela, width=770, height=50, background=co6, relief='flat')
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsq = Frame(janela, width=150, height=265, background=co4, relief='solid')
frameEsq.grid(row=1, column=0, sticky=NSEW)

frameDir = Frame(janela, width=600, height=265, background=co1, relief='raised')
frameDir.grid(row=1, column=1, sticky=NSEW)

#Logo ----------
#abrindo a imagem
app_img = Image.open('shopiconPI.png') 
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6,fg=co1)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Sistema de Gerenciamento de Estoque", compound=LEFT, padx=5, anchor=NW,font=('Verdana 15 bold'),bg=co6, fg=co1)
app_.place(x=50, y=7)  #ALTERAR

app_linha = Label(frameCima, width=770, height=1, padx=5, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
app_linha.place(x=0, y=47)


# Cadastro de Clientes 
def novo_cliente():
    global img_salvar

    def add():
        nome = e_nome.get()        # Nome do cliente
        email = e_email.get()      # Email
        telefone = e_telefone.get()  # Telefone

        # Verificar se os campos estão preenchidos
        lista = [nome, email, telefone]
        for i in lista:
            if i == '':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return

        # Inserir cliente no banco de dados
        insert_cliente(nome, '', '', email, telefone)

        messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso.')

        # Limpar os campos
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)

    # Interface gráfica do formulário de cadastro de clientes
    app_ = Label(frameDir, text='Cadastrar novo cliente', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    # Nome do cliente
    l_nome = Label(frameDir, text='Nome do cliente*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_nome = Entry(frameDir, width=25, justify='left', relief='solid')
    e_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    # Email do cliente
    l_email = Label(frameDir, text='Email do cliente*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_email = Entry(frameDir, width=25, justify='left', relief='solid')
    e_email.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    # Telefone do cliente
    l_telefone = Label(frameDir, text='Telefone do cliente*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_telefone.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_telefone = Entry(frameDir, width=25, justify='left', relief='solid')
    e_telefone.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    # Botão salvar
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=co1, fg=co4,
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=5, column=1, pady=5, sticky=NSEW)


# Exibir Clientes 
def ver_clientes():
    app_ = Label(frameDir, text='Ver clientes', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_clientes()

    # Criando a treeview com barra de rolagem dupla
    list_header = ['ID', 'Nome', 'Email', 'Telefone']
    
    global tree 
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    # Scrollbars
    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(0, weight=12)

    # Configurar colunas e cabeçalhos
    hd = ["nw", "nw", "nw", "nw"]
    h = [20, 120, 120, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # Inserir dados na treeview
    for item in dados:
        tree.insert('', 'end', values=item)


# Novo item 
def novo_item():  # Cadastro de Itens
    global img_salvar

    def add():
        nome = e_nome.get()        # Nome do item
        descricao = e_descricao.get()  # Descrição
        tamanho = e_tamanho.get()      # Tamanho
        cor = e_cor.get()          # Cor
        preco = e_preco.get()      # Preço
        quantidade = e_quantidade.get()  # Quantidade em estoque

        lista = [nome, descricao, tamanho, cor, preco, quantidade]

        # Verificando se há algum campo vazio ou não
        for i in lista:
            if i == '':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return
        # Inserindo os dados no banco de dados
        insert_item(nome, descricao, tamanho, cor, preco, quantidade)

        messagebox.showinfo('Sucesso', 'Item inserido com sucesso')

        # Limpando os campos de entrada
        e_nome.delete(0, END)
        e_descricao.delete(0, END)
        e_tamanho.delete(0, END)
        e_cor.delete(0, END)
        e_preco.delete(0, END)
        e_quantidade.delete(0, END)

    app_ = Label(frameDir, text='Inserir um novo item', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    # Criando formulário de preenchimento
    l_nome = Label(frameDir, text='Nome do item*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_nome = Entry(frameDir, width=25, justify='left', relief='solid')
    e_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_descricao = Label(frameDir, text='Descrição*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_descricao.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_descricao = Entry(frameDir, width=25, justify='left', relief='solid')
    e_descricao.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_tamanho = Label(frameDir, text='Tamanho*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_tamanho.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_tamanho = Entry(frameDir, width=25, justify='left', relief='solid')
    e_tamanho.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_cor = Label(frameDir, text='Cor*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cor.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    e_cor = Entry(frameDir, width=25, justify='left', relief='solid')
    e_cor.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_preco = Label(frameDir, text='Preço*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_preco.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)

    e_preco = Entry(frameDir, width=25, justify='left', relief='solid')
    e_preco.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    l_quantidade = Label(frameDir, text='Quantidade em estoque*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_quantidade.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)

    e_quantidade = Entry(frameDir, width=25, justify='left', relief='solid')
    e_quantidade.grid(row=7, column=1, padx=5, pady=5, sticky=NSEW)

    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=co1, fg=co4,
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=8, column=1, pady=5, sticky=NSEW)

# ver itens inseridos
def ver_itens():
    app_ = Label(frameDir, text='Todos os itens', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_itens()

    list_header = ['ID', 'Nome', 'Descrição', 'Tamanho', 'Cor', 'Preço', 'Quantidade em Estoque']
    
    global tree 
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 80, 150, 50, 60, 70, 50]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)


# realizar venda
def realizar_venda():
    global img_salvar

    def add():
        id_cliente = e_id_cliente.get()  # ID do cliente
        id_item = e_id_item.get()        # ID do item
        quantidade = e_quantidade.get()  # Quantidade vendida
        data_venda = hoje                # Data da venda

        lista = [id_cliente, id_item, quantidade]

        # Verificando se há algum campo não preenchido
        for i in lista:
            if i == '':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return

        # Inserindo os dados da venda no banco de dados
        insert_venda(id_cliente, id_item, data_venda, quantidade)
        # Atualizando o estoque do item após a venda
        update_item_estoque(id_item, quantidade)

        messagebox.showinfo('Sucesso', 'Venda realizada com sucesso.')

        # Limpando os campos de entrada
        e_id_cliente.delete(0, END)
        e_id_item.delete(0, END)
        e_quantidade.delete(0, END)

    # Interface gráfica da função de realizar venda
    app_ = Label(frameDir, text='Realizar uma venda', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    # Criando o formulário para venda
    l_id_cliente = Label(frameDir, text='Digite o ID do cliente*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_cliente.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_id_cliente = Entry(frameDir, width=25, justify='left', relief='solid')
    e_id_cliente.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_id_item = Label(frameDir, text='Digite o ID do item*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_item.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_id_item = Entry(frameDir, width=25, justify='left', relief='solid')
    e_id_item.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_quantidade = Label(frameDir, text='Quantidade vendida*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_quantidade.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_quantidade = Entry(frameDir, width=25, justify='left', relief='solid')
    e_quantidade.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    # Botão salvar venda
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=co1, fg=co4,
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=5, column=1, pady=5, sticky=NSEW)


#ver vendas
def ver_vendas():
    app_ = Label(frameDir, text='Vendas realizadas', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_itens_vendidos()

    list_header = ['ID Venda', 'Item', 'Cliente', 'Data da Venda', 'Quantidade Vendida']
    
    global tree 
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw"]
    h = [20, 100, 100, 100, 80]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)



#Função para controlar o Menu ------
def control(i):
    if i == 'novo_cliente':
        for widget in frameDir.winfo_children():
            widget.destroy()
        novo_cliente()

    if i == 'ver_clientes':
        for widget in frameDir.winfo_children():
            widget.destroy()
        ver_clientes()

    if i == 'novo_item':
        for widget in frameDir.winfo_children():
            widget.destroy()
        novo_item()

    if i == 'ver_itens':
        for widget in frameDir.winfo_children():
            widget.destroy()
        ver_itens()

    if i == 'realizar_venda':
        for widget in frameDir.winfo_children():
            widget.destroy()
        realizar_venda()

    if i == 'ver_vendas':
        for widget in frameDir.winfo_children():
            widget.destroy()
        ver_vendas()


#Menu ---------
# Novo cliente
img_cliente = Image.open('addiconPI.png')
img_cliente = img_cliente.resize((18, 18))
img_cliente = ImageTk.PhotoImage(img_cliente)
#criando botao do novo cliente
b_novo_cliente = Button(frameEsq, command=lambda:control('novo_cliente'), image=img_cliente, compound=LEFT, anchor=NW, text=' Novo cliente', bg=co4, fg=co1,
                        font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_cliente.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo item
img_novo_item = Image.open('addiconPI.png')
img_novo_item = img_novo_item.resize((18, 18))
img_novo_item = ImageTk.PhotoImage(img_novo_item)
#criando botao do novo item
b_novo_item = Button(frameEsq, command=lambda:control('novo_item'), image=img_novo_item, compound=LEFT, anchor=NW, text=' Novo item', bg=co4, fg=co1,
                     font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_item.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

#Ver itens
img_ver_itens = Image.open('produtoiconPI.png')
img_ver_itens = img_ver_itens.resize((18, 18))
img_ver_itens = ImageTk.PhotoImage(img_ver_itens)
#criando botao de ver os itens
b_ver_itens = Button(frameEsq, command=lambda:control('ver_itens'), image=img_ver_itens, compound=LEFT, anchor=NW, text=' Exibir todos os itens', bg=co4, fg=co1,
                     font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_itens.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)
#Ver todos clientes
img_ver_clientes = Image.open('usericonPI.png')
img_ver_clientes = img_ver_clientes.resize((18, 18))
img_ver_clientes = ImageTk.PhotoImage(img_ver_clientes)
#criando botao de ver os clientes
b_ver_clientes = Button(frameEsq, command=lambda:control('ver_clientes'), image=img_ver_clientes, compound=LEFT, anchor=NW, text=' Ver clientes', bg=co4, fg=co1,
                        font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_clientes.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

#Realizar venda
img_realizar_venda = Image.open('vendaiconPI.png')
img_realizar_venda = img_realizar_venda.resize((18, 18))
img_realizar_venda = ImageTk.PhotoImage(img_realizar_venda)
#criando botao de realizar venda
b_realizar_venda = Button(frameEsq, command=lambda:control('realizar_venda'), image=img_realizar_venda, compound=LEFT, anchor=NW, text=' Realizar uma venda', bg=co4, fg=co1,
                          font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_realizar_venda.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)


#Ver vendas
img_ver_venda = Image.open('carrinhoiconPI.png')
img_ver_venda = img_ver_venda.resize((18, 18))
img_ver_venda = ImageTk.PhotoImage(img_ver_venda)
#criando botao de ver vendas
b_ver_vendas = Button(frameEsq, command=lambda:control('ver_vendas'), image=img_ver_venda, compound=LEFT, anchor=NW, text=' Vendas realizadas', bg=co4, fg=co1,
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_vendas.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)



"""
esse método inicia o loop principal da interface gráfica. Enquanto esse loop está rodando,
a janela permanecerá aberta e interativa, esperando por eventos como cliques de botão, digitação de texto, redimensionamento da janela, etc.
em mainloop(), a janela da aplicação não aparecerá nem responderá a qualquer interação do usuário. Ele é fundamental para manter a interface gráfica ativa e funcional.
"""
janela.mainloop()