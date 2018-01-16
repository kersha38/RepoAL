# -*- coding: utf-8 -*-
from Tkinter import *
import probaMySQL as sql
import easygui as eg
import os

i = 0

def cargartabla(campo,valor):
    print 'Argumentos: ',campo,valor
    def addrow(arr, n):
        global i
        for j in range(n):
            e = Entry(venta, relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, arr[j])
        i += 1

    def busqueda():
        # criterio=Raw_input("Ingrese criterio de busqueda")
        query = "Select o.titulo, o.DESCRIPCION,u.nombre,u.INSTITUCION,o.FECHA_CREACION,o.PALABRAS_CLAVE from objeto_aprendijzaje o, usuario u where o.ID_U=u.ID_U and "+\
                campo+" like '"+valor+"';"
        print query
        resultado = sql.run_query(query)
        print(resultado)
        return resultado



    def borrar():
        # criterio = Raw_input("Ingrese criterio para eliminar: ")
        title=eg.enterbox(msg='Ingrese titulo', title='Borrar')
        query = "DELETE * from objeto_aprendijzaje where titulo like "+title
        sql.run_query(query)

    def editA():
        os.system('start C:\Users\wendy\Documents\GitHub\RepoAL\ejemplos_de_exe_learning\libertades.elp')

    def openA():
        title = eg.enterbox(msg='Ingrese titulo', title='Bajar')

    # ventana principal
    venta = Toplevel()
    venta.geometry("1200x500+0+0")
    venta.title("Tabla de resultados")


    Titulos = ['Nombre del OA', 'Descripcion', 'Autor', 'Intitucion', 'Fecha subida Rep',
               'Palabras clave']

    addrow(Titulos, 6)
    bBorrar = Button(venta, text="Borrar", command=borrar)
    bBorrar.grid(row=900, column=900)

    bEdit = Button(venta, text="Editar", command=editA)
    bEdit.grid(row=900, column=950)

    bDesr = Button(venta, text="Desempaquetar", command=openA)
    bDesr.grid(row=900, column=1000)

    # consulto
    filas = busqueda()

    # añado filas
    for fila in filas:
        addrow(fila, 6)

    #mainloop()


