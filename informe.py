# -*- coding: utf-8 -*-
import Tkinter as tk
import easygui as eg
import probaMySQL
import ttk
import login

ventaInfor= tk.Tk()
ventaInfor.geometry("500x250")
ventaInfor.title("Registrarse")
ventaInfor.configure(background="CadetBlue")

nombreLbl=tk.Label(ventaInfor, text="Nombre").place(x=10,y=10)
nombreEnt=tk.Entry(ventaInfor).place(x=70,y=10)

apellidoLbl=tk.Label(ventaInfor, text="Apellido").place(x=230,y=10)
apellidoEnt=tk.Entry(ventaInfor).place(x=290,y=10)

contraseLbl=tk.Label(ventaInfor, text="Contrasenia").place(x=10,y=40)
contraseEnt=tk.Entry(ventaInfor).place(x=90,y=40)

fechaNaciLabl=tk.Label(ventaInfor, text="Fecha de nacimiento").place(x=230,y=40)
fechaNaciEnt=tk.Entry(ventaInfor).place(x=360,y=40)

tipoUsuarioLbl=tk.Label(ventaInfor,text="Tipo").place(x=10,y=70)
tipoCombo=ttk.Combobox(ventaInfor)
tipoCombo.place(x=70, y=70)
tipoCombo["values"] = ["Administrador", "Profesor", "Estudiante"]

registrarButton=tk.Button(ventaInfor, text="Terminado", command=login).place(x=300,y=150)
ventaInfor.mainloop()
