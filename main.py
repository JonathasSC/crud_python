import mysql.connector
from tkinter import *
from tkinter import ttk

# CONEXÃO DATA BASE
conexao = mysql.connector.connect(
	host="XXXXXXX",
	user="XXXXXXX",
	password="XXXXXXX",
	database="XXXXXXX"
)

elementos = []
ident = []
nome = []
valor = []

cursor = conexao.cursor() 

# FUNÇÕES DO CRUD
def create():
	try:
		nome_produto = input_nome.get()
		desc_produto = input_desc.get()
		valor_produto = input_valor.get()

		comando = f'INSERT INTO produtos (nome_produto,descrição_produto,valor) VALUES ("{nome_produto}","{desc_produto}",{valor_produto})'
		
		cursor.execute(comando)
		conexao.commit()

	except RuntimeError:
		texto_aviso['text'] = "ERROR"
	
	read()

def read():
	try:
		comando = f'SELECT * FROM produtos'

		cursor.execute(comando)
		result = cursor.fetchall()

		tree_view.delete(*tree_view.get_children())

		for linha in result:
			elementos = [linha[0],linha[1],linha[2],linha[3]]
			tree_view.insert("",END, values=elementos,tag=1)
		

	except RuntimeError:
		texto_aviso['text'] = "ERROR"
		

def update():
	try:
		nome_produto = input_nome.get()
		valor_produto = input_valor.get()

		comando = f'UPDATE produtos SET valor = {valor_produto} WHERE nome_produto = "{nome_produto}"'

		cursor.execute(comando)
		conexao.commit()

	except RuntimeError:
		texto_aviso['text'] = "ERROR"


def delete():
	try:
		nome_produto = input_nome.get()

		comando = f'DELETE FROM produtos WHERE nome_produto = "{nome_produto}"'

		cursor.execute(comando)
		conexao.commit()

	except RuntimeError:
		texto_aviso['text'] = "ERROR"

	read()
# INTERFACE

window = Tk()

window.geometry("900x600+200+50")

window.title("CRUD")

tela_principal = Frame(window, bg='#353535')
tela_principal.pack(fill=BOTH, expand=1)


titulo_app = Label(tela_principal,text="CRUD - JP pescados", font=("Arial Black",20),bg="#353535", fg="white")
titulo_app.place(x=299, y=20)


#INPUT NOME
produto_label = Label(tela_principal, text="Nome", font =('Arial Black', 12), bg="#353535",fg="white")
produto_label.place(x=20,y=216)

input_nome = Entry(tela_principal, width=23, font=1)
input_nome.place(x=100, y=220)


#INPUT DESC
valor_label = Label(tela_principal, text="Valor", font =('Arial Black', 12), bg="#353535",fg="white")
valor_label.place(x=20,y=270)

input_valor = Entry(tela_principal, width=23, font=1)
input_valor.place(x=100, y=274)

#INPUT DESC
desc_label = Label(tela_principal, text="Desc", font =('Arial Black', 12), bg="#353535",fg="white")
desc_label.place(x=20,y=330)

input_desc = Entry(tela_principal, width=23, font=1)
input_desc.place(x=100, y=330)

#BOTÕES
botao_c = Button(window, text="create", command=create, bd=0, bg="#0EC711", fg="white",font =('Arial Black', 9))
botao_r = Button(window, text="read",command=read, bd=0, bg="#F8AC4A", fg="white",font =('Arial Black', 9))
botao_u = Button(window, text="update", command=update, bd=0, bg="#0EC7E6", fg="white",font =('Arial Black', 9))
botao_d = Button(window, text="delete", command=delete, bd=0, bg="#D62C1A", fg="white",font =('Arial Black', 9))

botao_c.place(x=20,y=380,width=80)
botao_r.place(x=125,y=380,width=80)
botao_u.place(x=230,y=380,width=80)
botao_d.place(x=20,y=430,width=290)


tree_view = ttk.Treeview(window, selectmode="browse", columns=("column1","column2","column3","column4"), show="headings", height=12)

tree_view.column("column1",width=50,minwidth=50,stretch=NO)
tree_view.heading("#1",text="ID")

tree_view.column("column2",width=100,minwidth=50,stretch=NO)
tree_view.heading("#2",text="produto")

tree_view.column("column3",width=220,minwidth=50,stretch=NO)
tree_view.heading("#3",text="descrição")

tree_view.column("column4",width=100,minwidth=50,stretch=NO)
tree_view.heading("#4",text="valor")

tree_view.place(x=400,y=200)

texto_aviso = Label(window, text='⠀⠀⠀', bg="#353535", fg="#353535")
texto_aviso.place(x=299, y=80)

window.mainloop()
cursor.close()
conexao.close()