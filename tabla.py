# -*- coding: utf-8 -*-
from Tkinter import *
import probaMySQL as sql


i=0
#ventana principal
venta=tk.Tk()
venta.geometry("1200x500+0+0")
venta.title("Tabla de resultados")



def addrow(arr,n):
    global i
    for j in range(n):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, arr[j])
    i+=1

def busqueda():
    #criterio=Raw_input("Ingrese criterio de busqueda")
    query="SELECT * from usuario"
    resultado= sql.run_query(query)
    print(resultado)
    return resultado

def borrar():
    #criterio = Raw_input("Ingrese criterio para eliminar: ")
    query = "DELETE * from usuario where nombre=andrea"
    sql.run_query(query)

Titulos=['Nombre del OA','Descripcion','Autor','Intitucion','Fecha de creacion',
         'Palabras clave','Tipo de archivo',
         'Fecha de ingreso al repositorio']


addrow(Titulos,8)
bBorrar=Button(venta,text="Borrar", command=borrar)
bBorrar.grid(row=900, column=900)

bEdit=Button(venta,text="Editar", command=borrar)
bEdit.grid(row=900, column=950)

bDesr=Button(venta,text="Desempaquetar", command=borrar)
bDesr.grid(row=900, column=1000)

#consulto
filas=busqueda()

#añado filas
for fila in filas:
    addrow(fila,2)

mainloop()

