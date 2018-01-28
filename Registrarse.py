# -*- coding: utf-8 -*-
import Tkinter as tk
import login
import informe


ventaRegis= tk.Tk()
ventaRegis.geometry("400x400")
ventaRegis.title("Iniciar Sesion/Registrarse")
img=tk.PhotoImage(file = "login.gif")
ventaRegis.configure(background= "CadetBlue")
lblimagen2 = tk.Label(ventaRegis, image=img).place(x=90, y=50)
LoginButton= tk.Button(ventaRegis, text="Iniciar Sesion", command=login.runLogin).place(x=150, y=300)
RegistraseButton= tk.Button(ventaRegis, text="Registrarse",command=informe).place(x=155,y=350)
ventaRegis.mainloop()