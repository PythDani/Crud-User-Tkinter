from tkinter import Tk, Button, Frame
import tkinter as tk 
from tkinter import *
from tkinter import messagebox
import mysql.connector


class Supermercado():
    
    def __init__(self):
        self.conexion = mysql.connector.connect(host ='127.0.0.1', user='root', passwd='toor', database='supermercado')
        self.cursor = self.conexion.cursor()
       # print(self.conexion) Para imprimir en consola la instancia de conexion
#mercado = Supermercado() Probamos conexión a base de datos


        self.ventana = Tk()
        self.ventana.title('Registro para clientes')
        self.ventana.geometry('700x300')
        self.ventana.resizable(False,False)
        self.ventana.config(background="#e0d7d7")
        Frame1 = Frame(self.ventana)
        Frame1.pack()

        nuevoButton = Button(Frame1, text= "Crear Nuevo Cliente",bg="#e0d7d7", fg="Black", font=("Tahoma",14))
        nuevoButton.pack()

        recuadro = LabelFrame(self.ventana, text ='Crear Usuario:   ')
        recuadro.pack()

        self.Id=IntVar()
        self.Nombres=StringVar()
        self.Apellidos=StringVar()
        self.Email=StringVar()

        Label0 = Label(recuadro, text ='Id: ', background="yellow",width=80).pack()
        Label00 = Entry (recuadro,width=20,textvariable=self.Id)
        Label00.pack()
        

        Label1 = Label(recuadro, text ='Nombres: ', background="yellow",width=80).pack()
        Label11 = Entry (recuadro,width=20,textvariable=self.Nombres)
        Label11.pack()
       
        Label2 = Label(recuadro, text ='Apellidos: ', background="yellow",width=80).pack()
        Label22= Entry(recuadro,width=20,textvariable=self.Apellidos)
        Label22.pack()
        
        Label3 = Label (recuadro, text ='Email ', background="yellow",width=80).pack()
        Label33 = Entry (recuadro,width=20,textvariable=self.Email)
        Label33.pack()

        Frame2 = Frame (self.ventana)
        Frame2.pack()

        GuardarButton = Button(Frame2, text= "Guardar",bg="#e0d7d7",command=self.insertar)
        GuardarButton.grid(row=0, column=0)

        CancelarButton = Button(Frame2,text= "Cancelar",bg="#e0d7d7",command=self.cancelar)
        CancelarButton.grid(row=0,column=1)
        
        self.EliminarButton = Button(Frame2,bg="#e0d7d7", text= "Eliminar Usuario",command=self.eliminar)
        self.EliminarButton.grid(row=0, column=2)

        self.actualizarButton = Button(Frame2,bg="#e0d7d7", text="Actualizar Usuario",command=self.actualizar)
        self.actualizarButton.grid(row=0, column=3)

        self.ventana.mainloop()

    def insertar (self):
        sql= 'insert into  usuarios (nombres, apellidos, email) values ("{}","{}","{}")'.format(self.Nombres.get(),self.Apellidos.get(), self.Email.get())
        self.cursor.execute(sql)
        self.conexion.commit()
        messagebox.showinfo("Advertencia","Su registro se ha generado con exito")
        self.Nombres.set("")
        self.Apellidos.set("")
        self.Email.set("")

    def cancelar(self):
        self.Nombres.set("")
        self.Apellidos.set("")
        self.Email.set("")
        messagebox.showinfo("Advertencia","Se ha eliminado con exito sus repuestas")

    def eliminar(self):
        try:
            sql1=('delete from usuarios where idusuarios = {}'.format(self.Id.get()))
            self.cursor.execute(sql1)
            self.conexion.commit()
            messagebox.showinfo("Advertencia","Su registro se ha eliminado con exito")
            self.Nombres.set("")
            self.Apellidos.set("")
            self.Cédula.set("")
        except:
            messagebox.showinfo("Advertencia","El registro no existe")
    
    def actualizar(self):
        sql3='update usuarios set nombres="{}", apellidos="{}", email="{}" where idusuarios="{}"'
        self.cursor.execute(sql3.format(self.Nombres.get(), self.Apellidos.get(), self.Email.get(), self.Id.get()))
        self.conexion.commit()
        messagebox.showinfo("Advertencia","Su registro se ha actualizado con exito")
       
        self.Nombres.set("")
        self.Apellidos.set("")
        self.Email.set("") 




   
mercado = Supermercado()


