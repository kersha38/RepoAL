# -*- coding: utf-8 -*-
import Tkinter as tk
import probaMySQL as ms
import ttk
import wCalendar


def run():
    fecha = {}

    def registrar():
        ms.run_query('insert into usuario(nombre,clave,tipo,FechaNaci) values(\"'+nombreEnt.get()+''+apellidoEnt.get()+'\",'
                     +'\"'+contraseEnt.get()+'\",'
                     + '\"' + contraseEnt.get() + '\",'
                     + '\"' + tipoCombo.get() + '\",'
                     + '\"' + repr(fecha['year_selected'])+'/'+repr(fecha['month_selected'])+'/'+repr(fecha['day_selected'])
                     +')')
        ventaInfor.destroy()

    def obFecha():
        child = tk.Toplevel()
        calendario = wCalendar.Calendar(child, fecha)

    ventaInfor = tk.Tk()
    ventaInfor.geometry("500x250")
    ventaInfor.title("Registrarse")
    ventaInfor.configure(background="CadetBlue")

    nombreLbl = tk.Label(ventaInfor, text="Nombre").place(x=10, y=10)
    nombreEnt = tk.Entry(ventaInfor).place(x=70, y=10)

    apellidoLbl = tk.Label(ventaInfor, text="Apellido").place(x=230, y=10)
    apellidoEnt = tk.Entry(ventaInfor).place(x=290, y=10)

    contraseLbl = tk.Label(ventaInfor, text="Clave de acceso").place(x=10, y=40)
    contraseEnt = tk.Entry(ventaInfor,show='*').place(x=90, y=40)

    btnFecha = tk.Button(ventaInfor, text="Fecha Nacimineto", fg="black", command=obFecha).place(x=360, y=40)
    #fechaNaciEnt = tk.Entry(ventaInfor).place(x=360, y=40)

    tipoUsuarioLbl = tk.Label(ventaInfor, text="Tipo").place(x=10, y=70)
    tipoCombo = ttk.Combobox(ventaInfor)
    tipoCombo.place(x=70, y=70)
    tipoCombo["values"] = ["Administrador", "Profesor", "Estudiante"]

    registrarButton = tk.Button(ventaInfor, text="Registrar", command=registrar).place(x=300, y=150)
    ventaInfor.mainloop()
