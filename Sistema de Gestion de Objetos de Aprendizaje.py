#import probaMySQL as msql
import Tkinter as tk
import tabla as tb
import intCargar


#ventana terciaria
def abrirBusqueda():

    # ventana de funcion buscar
    def Buscar():
        titu=['o.titulo','u.nombre','o.FECHA_CREACION','o.PALABRAS_CLAVE']
        tb.cargartabla(titu[lstCamoo.curselection()[0]],campo_text.get())
        # tb.addrow()

    ventaBus=tk.Tk()
    ventaBus.geometry("500x500+200+200")
    ventaBus.title("Busqueda")
    lblcampo = tk.Label(ventaBus, text="Escoger campo").place(x=20, y=50)
    lstCamoo = tk.Listbox(ventaBus, width=20)
    lstCamoo.insert(0, "Titulo")
    lstCamoo.insert(1, "Autor")
    lstCamoo.insert(2, "Fecha de creacion")
    lstCamoo.insert(3, "Palabra clave")
    lstCamoo.place(x=20, y=70)
    botonB=tk.Button(ventaBus, text="Buscar", command=Buscar)
    botonB.place(x=200,y=50)
    botonB.pack()
    campo_text = tk.Entry(ventaBus)
    campo_text.pack()
    campo_text.get()



#ventana secundaria
def abrirVentana():
    ventAV=tk.Tk()
    ventAV.geometry("300x300+100+100")
    ventAV.title("Opciones")
    lblOpciones=tk.Label(ventAV,text="Escoger una opcion").place(x=50,y=50)
    select=tk.IntVar()
    rdBOP=tk.Radiobutton(ventAV, text="Importar y catalogar OA",command=intCargar.cargar,value=1,variable=select).place(x=50,y=100)
    rdBOP = tk.Radiobutton(ventAV, text="Busqueda de OA", value=2,variable=select,command=abrirBusqueda).place(x=50, y=150)
    ventAV.mainloop()

#ventan contenedora global
ventana=tk.Tk()
ventana.geometry("700x500+0+0")
ventana.title("Sistema de Gestion de Objetos de Aprendizaje")
ventana.configure(background="grey")

#crear el  menu
barraMenu=tk.Menu(ventana)
mnuMenu=tk.Menu(barraMenu)
mnuMenu.add_command(label= "Crear Objeto de Aprendizaje")
mnuMenu.add_command(label= "Repositorio Objeto de Aprendizaje",command=abrirVentana)
mnuMenu.add_command(label= "Salir",command=ventana.destroy)
barraMenu.add_cascade(label= "Menu" ,menu=mnuMenu)
ventana.config(menu=barraMenu)
ventana.mainloop()