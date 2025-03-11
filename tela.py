#Descrição: Sistema de Gerenciamento de Estoque de um Brécho.
#Data de criação: 20/09/2024
#Autor: Nicolly Mendes

from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import date
from datetime import datetime
from tkinter.ttk import Combobox
import re
# importando as funções da view
from view import *

hoje = date.today()

# CORES
co0 = "#0D1B2A"  # Cor 1
co1 = "#E0E1DD"  # Cor 5 (Fundo neutro claro)
co2 = "#4fa882"  # Manter (Verde)
co3 = "#415A77"  # Cor 3 (Barra separadora)
co4 = "#1B263B"  # Cor 2 (Fundo de botões e painéis laterais)
co5 = "#e06636"  # Manter (Para lucro/profit)
co6 = "#778DA9"  # Cor 4 (Cabeçalho)
co7 = "#3fbfb9"  # Manter (Verde)
co8 = "#263238"  # Manter (Escuro adicional)
co9 = "#E0E1DD"  # Mesma da cor 5 (Fundo claro)
co10 = "#6e8faf" # Manter
co11 = "#f2f4f2" # Manter

# Criando janela  ------
janela = Tk()
janela.title('Sistema Responsivo de Gerenciamento de Estoque')
janela.geometry('770x330')  # Tamanho inicial maior para testar a responsividade
janela.configure(background=co1)
janela.resizable(True, True)  # Permitir redimensionamento

style = Style(janela)
style.theme_use('clam')

# Configurar o layout da janela para expandir conforme o tamanho
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=3)
janela.grid_rowconfigure(1, weight=1)

# Frames ------
frameCima = Frame(janela, background=co6, relief='flat')
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsq = Frame(janela, background=co4, relief='solid')
frameEsq.grid(row=1, column=0, sticky=NSEW)

frameDir = Frame(janela, background=co1, relief='raised')
frameDir.grid(row=1, column=1, sticky=NSEW)

# Responsividade dos frames
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=3)  # Frame da direita ocupa mais espaço
janela.grid_rowconfigure(1, weight=1)

frameEsq.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
frameEsq.grid_columnconfigure(0, weight=1)

frameDir.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
frameDir.grid_columnconfigure(0, weight=1)
frameDir.grid_columnconfigure(1, weight=3)  # Adiciona peso para expandir melhor as caixas de texto

# Logo ----------
app_img = Image.open('shopiconPI.png') 
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
app_logo.grid(row=0, column=0, sticky="nsew")

app_ = Label(frameCima, text="Sistema de Gerenciamento de Estoque", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
app_.grid(row=0, column=1, sticky="nsew")

# Linha separadora
app_linha = Label(frameCima, height=1, padx=5, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
app_linha.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Função para validar CPF
def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)  # Remove todos os caracteres não numéricos
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * len(cpf):
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 < 10 else 0

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_2 = (soma * 10) % 11
    digito_2 = digito_2 if digito_2 < 10 else 0

    return cpf[-2:] == f"{digito_1}{digito_2}"

# Função para cadastro de novo cliente com layout responsivo
def novo_cliente():
    global img_salvar

    def add():
        nome = e_nome.get()
        cpf = e_cpf.get()
        cep = e_cep.get()
        endereco = e_endereco.get()
        complemento = e_complemento.get()
        uf = combo_uf.get()
        email = e_email.get()
        telefone = e_telefone.get()

        lista = [nome, cpf, cep, endereco, uf, email, telefone]

        for campo in lista:
            if campo == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        if not validar_cpf(cpf):
            messagebox.showerror('Erro', 'CPF inválido. Insira um CPF válido.')
            return

        insert_cliente(nome, cpf, cep, endereco, complemento, uf, email, telefone)
        messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso')
        
        # Limpar os campos após inserção
        e_nome.delete(0, END)
        e_cpf.delete(0, END)
        e_cep.delete(0, END)
        e_endereco.delete(0, END)
        e_complemento.delete(0, END)
        combo_uf.set('')  
        e_email.delete(0, END)
        e_telefone.delete(0, END)

    # Interface gráfica do formulário de cliente
    for widget in frameDir.winfo_children():
        widget.destroy()

    app_ = Label(frameDir, text='Cadastrar novo cliente', width=50, compound=LEFT, padx=5, pady=5, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    # Responsividade dos widgets
    frameDir.grid_rowconfigure(0, weight=1)
    frameDir.grid_rowconfigure([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weight=1)
    frameDir.grid_columnconfigure(0, weight=1)
    frameDir.grid_columnconfigure(1, weight=2)

    # Nome do cliente
    l_nome = Label(frameDir, text='Nome do cliente*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)

    e_nome = Entry(frameDir, justify='left', relief='solid')
    e_nome.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    # CPF do cliente
    l_cpf = Label(frameDir, text='CPF*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cpf.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_cpf = Entry(frameDir, justify='left', relief='solid')
    e_cpf.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    # CEP do cliente
    l_cep = Label(frameDir, text='CEP*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cep.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_cep = Entry(frameDir, justify='left', relief='solid')
    e_cep.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    # Endereço do cliente
    l_endereco = Label(frameDir, text='Endereço*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_endereco = Entry(frameDir, justify='left', relief='solid')
    e_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    # Complemento do endereço
    l_complemento = Label(frameDir, text='Complemento', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_complemento.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    e_complemento = Entry(frameDir, justify='left', relief='solid')
    e_complemento.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    # UF do cliente (Combobox)
    l_uf = Label(frameDir, text='UF*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_uf.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)

    combo_uf = Combobox(frameDir, state='readonly')
    combo_uf['values'] = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    combo_uf.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    # Email do cliente
    l_email = Label(frameDir, text='Email*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)

    e_email = Entry(frameDir, justify='left', relief='solid')
    e_email.grid(row=7, column=1, padx=5, pady=5, sticky=NSEW)

    # Telefone do cliente
    l_telefone = Label(frameDir, text='Telefone*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_telefone.grid(row=8, column=0, padx=5, pady=5, sticky=NSEW)

    e_telefone = Entry(frameDir, justify='left', relief='solid')
    e_telefone.grid(row=8, column=1, padx=5, pady=5, sticky=NSEW)

    # Botão salvar
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir, command=add, image=img_salvar, compound=LEFT, anchor=NW, text=' Salvar', bg=co1, \
                      fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=9, column=1, pady=5, sticky=NSEW)




# Exibir Clientes 
def ver_clientes():
    app_ = Label(frameDir, text='Ver clientes', width=50, compound=LEFT, padx=5, pady=5, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_clientes()  # Aqui você chama a função que busca os clientes no banco de dados.

    # Criando a Treeview com scrollbar para exibir os dados dos clientes
    list_header = ['ID', 'Nome', 'CPF', 'Email', 'Telefone']

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
    h = [30, 150, 120, 180, 120]  # Ajuste os tamanhos das colunas conforme a necessidade
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

# Função para cadastrar um novo item com layout responsivo
def novo_item():
    global img_salvar

    def add():
        nome = e_nome.get()
        descricao = e_descricao.get()
        tipo_peca = combo_tipo.get()
        tamanho = combo_tamanho.get()
        cor = e_cor.get()
        preco = e_preco.get()
        quantidade = e_quantidade.get()

        lista = [nome, descricao, tipo_peca, tamanho, cor, preco, quantidade]

        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        insert_item(nome, descricao, tamanho, cor, preco, quantidade)
        messagebox.showinfo('Sucesso', 'Item inserido com sucesso')
        e_nome.delete(0, END)
        e_descricao.delete(0, END)
        combo_tipo.set('')
        combo_tamanho.set('')
        e_cor.delete(0, END)
        e_preco.delete(0, END)
        e_quantidade.delete(0, END)

    def atualizar_tamanhos(event):
        tipo_peca = combo_tipo.get()
        if tipo_peca == "Vestuário":
            combo_tamanho['values'] = ["PP", "P", "M", "G", "GG"]
        elif tipo_peca == "Calçado":
            combo_tamanho['values'] = list(range(36, 45))
        else:
            combo_tamanho['values'] = []

    # Interface gráfica
    for widget in frameDir.winfo_children():
        widget.destroy()

    app_ = Label(frameDir, text='Inserir um novo item', width=50, compound=LEFT, padx=5, pady=5, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    # Responsividade
    frameDir.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)
    frameDir.grid_columnconfigure(0, weight=1)
    frameDir.grid_columnconfigure(1, weight=2)

    # Nome do item
    l_nome = Label(frameDir, text='Nome do item*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)

    e_nome = Entry(frameDir, justify='left', relief='solid')
    e_nome.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    # Descrição
    l_descricao = Label(frameDir, text='Descrição*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_descricao.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_descricao = Entry(frameDir, justify='left', relief='solid')
    e_descricao.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    # Tipo de peça
    l_tipo = Label(frameDir, text='Tipo da peça*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_tipo.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    combo_tipo = Combobox(frameDir, state='readonly')
    combo_tipo['values'] = ["Vestuário", "Calçado"]
    combo_tipo.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)
    combo_tipo.bind("<<ComboboxSelected>>", atualizar_tamanhos)

    # Tamanho
    l_tamanho = Label(frameDir, text='Tamanho*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_tamanho.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    combo_tamanho = Combobox(frameDir, state='readonly')
    combo_tamanho.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    # Cor
    l_cor = Label(frameDir, text='Cor*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cor.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    e_cor = Entry(frameDir, justify='left', relief='solid')
    e_cor.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    # Preço
    l_preco = Label(frameDir, text='Preço*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_preco.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)

    e_preco = Entry(frameDir, justify='left', relief='solid')
    e_preco.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    # Quantidade
    l_quantidade = Label(frameDir, text='Quantidade em estoque*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_quantidade.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)

    e_quantidade = Entry(frameDir, justify='left', relief='solid')
    e_quantidade.grid(row=7, column=1, padx=5, pady=5, sticky=NSEW)

    # Botão salvar
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir, command=add, image=img_salvar, compound=LEFT, anchor=NW, \
                      text=' Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=8, column=1, pady=5, sticky=NSEW)



# Função para exibir os itens cadastrados com layout responsivo
def ver_itens():
    for widget in frameDir.winfo_children():
        widget.destroy()

    app_ = Label(frameDir, text='Todos os itens', width=50, compound=LEFT, padx=5, pady=5, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    dados = get_itens()

    list_header = ['ID', 'Nome', 'Descrição', 'Tamanho', 'Cor', 'Preço', 'Quantidade em Estoque']
    
    global tree 
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frameDir.grid_rowconfigure(1, weight=1)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 80, 150, 50, 60, 70, 50]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)



# Função para realizar uma venda com layout responsivo
def realizar_venda():
    global img_salvar

    def add():
        cliente_selecionado = combo_cliente.get()
        item_selecionado = combo_item.get()
        quantidade = e_quantidade.get()
        data_venda = hoje

        id_cliente = cliente_selecionado.split(" - ")[0]
        id_item = item_selecionado.split(" - ")[0]

        if id_cliente == '' or id_item == '' or quantidade == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

        insert_venda(id_cliente, id_item, data_venda, quantidade)
        update_item_estoque(id_item, quantidade)
        messagebox.showinfo('Sucesso', 'Venda realizada com sucesso.')

        combo_cliente.set('')
        combo_item.set('')
        e_quantidade.delete(0, END)

    for widget in frameDir.winfo_children():
        widget.destroy()

    app_ = Label(frameDir, text='Realizar uma venda', width=50, compound=LEFT, padx=5, pady=5, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    # Responsividade
    frameDir.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)
    frameDir.grid_columnconfigure(0, weight=1)
    frameDir.grid_columnconfigure(1, weight=2)

    # Cliente
    l_cliente = Label(frameDir, text='Selecione o cliente*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cliente.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)

    combo_cliente = Combobox(frameDir, width=25)
    combo_cliente.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    # Item
    l_item = Label(frameDir, text='Selecione o item*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_item.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    combo_item = Combobox(frameDir, width=25)
    combo_item.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    # Quantidade
    l_quantidade = Label(frameDir, text='Quantidade vendida*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_quantidade.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_quantidade = Entry(frameDir, justify='left', relief='solid')
    e_quantidade.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    # Botão salvar venda
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir, command=add, image=img_salvar, compound=LEFT, anchor=NW, text=' Salvar', bg=co1, fg=co4, \
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=4, column=1, pady=5, sticky=NSEW)

    preencher_comboboxes(combo_cliente, combo_item)



# Função para exibir as vendas realizadas com o valor total gasto
def ver_vendas():
    # Limpa o frame
    for widget in frameDir.winfo_children():
        widget.destroy()

    # Título
    app_ = Label(frameDir, text='Vendas realizadas', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=5, sticky=NSEW)

    # Linha separadora
    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=5, sticky=NSEW)

    # Recupera os dados das vendas e calcula o valor total de cada venda
    vendas = get_itens_vendidos()
    
    # Verificação básica se há dados
    if not vendas:
        messagebox.showinfo('Info', 'Nenhuma venda realizada até agora.')
        return

    lista_vendas = []
    
    for venda in vendas:
        id_venda = venda[0]
        nome_item = venda[1]
        nome_cliente = venda[2] 
        data_venda = venda[3]
        quantidade_vendida = venda[4]
        preco_item = venda[5]

        # Substitui vírgula por ponto no preço e tenta converter para float
        try:
            quantidade_vendida = int(quantidade_vendida)  # Converte para inteiro
            preco_item = float(preco_item.replace(',', '.'))  # Substitui a vírgula por ponto e converte para float
        except ValueError as e:
            print(f"Erro de conversão em quantidade ou preço: {e}")
            messagebox.showerror('Erro', f"Falha ao processar a venda com ID {id_venda}. Verifique os dados.")
            return
        
        # Calcula o valor total
        valor_total = quantidade_vendida * preco_item

        # Adiciona os dados da venda na lista
        lista_vendas.append((id_venda, nome_item, nome_cliente, data_venda, quantidade_vendida, f'R${valor_total:.2f}'))

    # Criando a Treeview com barra de rolagem para exibir os dados das vendas
    list_header = ['ID Venda', 'Item', 'Cliente', 'Data da Venda', 'Quantidade Vendida', 'Valor Total']

    global tree
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    # Configurando as barras de rolagem
    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posiciona a Treeview e as barras de rolagem
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(2, weight=1)

    # Definindo as larguras e cabeçalhos das colunas
    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [50, 150, 150, 100, 100, 120]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # Inserindo os dados das vendas na Treeview
    for item in lista_vendas:
        tree.insert('', 'end', values=item)
        
# Função para criar o backup do banco de dados
def realizar_backup():
    # Define o diretório de backup
    diretorio_backup = 'backups'

    # Verifica se o diretório de backup exite, caso contrário, cria-o
    if not os.path.exists(diretorio_backup):
        os.makedirs(diretorio_backup)

    # Nome do arquivo orignal do banco de dados
    arquivo_origem = 'dados/dados_brecho.db'

    # Nome do arquivo de backup com data e hora
    data_atual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    arquivo_backup = f'{diretorio_backup}/backup_{data_atual}.db'
    # Realiza a cópia do arquivo de origem para o diretorio de backuo
    shutil.copy2(arquivo_origem, arquivo_backup)
    print(f'Backup realizado com sucesso : {arquivo_backup}')
    
# Função para controlar o Menu ------
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


# Menu ---------
# Novo cliente
img_cliente = Image.open('addiconPI.png')
img_cliente = img_cliente.resize((18, 18))
img_cliente = ImageTk.PhotoImage(img_cliente)
b_novo_cliente = Button(frameEsq, command=lambda:control('novo_cliente'), image=img_cliente, compound=LEFT, \
                        anchor=NW, text=' Novo cliente', bg=co4, fg=co1,
                        font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_cliente.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo item
img_novo_item = Image.open('addiconPI.png')
img_novo_item = img_novo_item.resize((18, 18))
img_novo_item = ImageTk.PhotoImage(img_novo_item)
b_novo_item = Button(frameEsq, command=lambda:control('novo_item'), image=img_novo_item, compound=LEFT, \
                     anchor=NW, text=' Novo item', bg=co4, fg=co1,
                     font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_item.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver itens
img_ver_itens = Image.open('produtoiconPI.png')
img_ver_itens = img_ver_itens.resize((18, 18))
img_ver_itens = ImageTk.PhotoImage(img_ver_itens)
b_ver_itens = Button(frameEsq, command=lambda:control('ver_itens'), image=img_ver_itens, compound=LEFT, \
                     anchor=NW, text=' Exibir todos os itens', bg=co4, fg=co1,
                     font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_itens.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Ver todos clientes
img_ver_clientes = Image.open('usericonPI.png')
img_ver_clientes = img_ver_clientes.resize((18, 18))
img_ver_clientes = ImageTk.PhotoImage(img_ver_clientes)
b_ver_clientes = Button(frameEsq, command=lambda:control('ver_clientes'), image=img_ver_clientes, \
                        compound=LEFT, anchor=NW, text=' Ver clientes', bg=co4, fg=co1,
                        font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_clientes.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar venda
img_realizar_venda = Image.open('vendaiconPI.png')
img_realizar_venda = img_realizar_venda.resize((18, 18))
img_realizar_venda = ImageTk.PhotoImage(img_realizar_venda)
b_realizar_venda = Button(frameEsq, command=lambda:control('realizar_venda'), image=img_realizar_venda,\
                          compound=LEFT, anchor=NW, text=' Realizar uma venda', bg=co4, fg=co1,
                          font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_realizar_venda.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Ver vendas
img_ver_venda = Image.open('carrinhoiconPI.png')
img_ver_venda = img_ver_venda.resize((18, 18))
img_ver_venda = ImageTk.PhotoImage(img_ver_venda)
b_ver_vendas = Button(frameEsq, command=lambda:control('ver_vendas'), image=img_ver_venda, \
                      compound=LEFT, anchor=NW, text=' Vendas realizadas', bg=co4, fg=co1,
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_vendas.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar backup ao nciar o programa
realizar_backup()

# Loop principal da interface gráfica
janela.mainloop()
