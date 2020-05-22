#import
from tkinter import *
from tkinter import messagebox, ttk
import database


#Construção da janela
janela = Tk()
janela.title("Sistema")
janela.configure(background="white")
janela.geometry("600x300")
janela.resizable(width = False, height = False)

#Funções
def registrar_banco():
    nome = nome_.get()
    email = email_.get()
    telefone = telefone_.get()
    database.cur.execute("""
    insert into login(nome,email,telefone) values(%s,%s,%s)
    """, (nome,email,telefone))
    database.con.commit()
    messagebox.showinfo(title="Cadastro", message="Dados inseridos com sucesso.")  
   
    print(nome_.get())
    print(email_.get())
    print(telefone_.get())
    label1['text'] = nome_.get()
    label2['text'] = email_.get()
    label3['text'] = telefone_.get()

    nome_.delete(0, END) 
    email_.delete(0, END)
    telefone_.delete(0, END)
   
#Frame
left = Frame(janela, width = 295, height = 400, bg="MIDNIGHTBLUE")
left.pack(side = LEFT)

right = Frame(janela, width = 300, height = 400, bg="MIDNIGHTBLUE")
right.pack(side = RIGHT)


#Label
nome = Label(left, text="Nome", font=("Comic Sans", 10), bg="MIDNIGHTBLUE", fg="green")
nome.place(x=10, y=50)

email = Label(left, text="E-mail", font=("Comic Sans", 10), bg="MIDNIGHTBLUE", fg="green")
email.place(x=10, y=80)

telefone = Label(left, text="Telefone", font=("Comic Sans", 10), bg="MIDNIGHTBLUE", fg="green")
telefone.place(x=10, y=110)


#Label show
label0 = Label(right, text="Visualização dos dados inseridos", font=("Comic Sans", 11), bg="MIDNIGHTBLUE", fg="white")
label0.place(x=20, y=10)

label1 = Label(right, text=" ", bg="MIDNIGHTBLUE", fg="red")
label1.place(x=20, y=50)

label2 = Label(right, text=" ", bg="MIDNIGHTBLUE", fg="red")
label2.place(x=20, y=80)

label3 = Label(right, text=" ", bg="MIDNIGHTBLUE", fg="red")
label3.place(x=20, y=110)

#Entry
nome_ = ttk.Entry(left, width=20)
nome_.place(x=90, y=50)

email_ = ttk.Entry(left, width=20)
email_.place(x=90, y=80)

telefone_ = ttk.Entry(left, width=20)
telefone_.place(x=90, y=110)

#Botão
registrar = ttk.Button(left, width=10, text="Registrar", command=registrar_banco)
registrar.place(x=90, y=140)

#Fim da janela
janela.mainloop()