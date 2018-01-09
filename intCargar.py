# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk
import probaMySQL
import easygui as eg
import wCalendar



def cargar():
    fecha = {}
    archivo = ''

    def guardarBase(institucion, nombreA, tituloO, Descripcion, Ruta, Fecha, PClave):
        query = "insert into usuario (nombre, Institucion) values (' "+ nombreA + "','" + institucion + "');"
        probaMySQL.run_query(query)

        query = "insert into objeto_aprendijzaje (id_u, titulo, descripcion, ruta,fecha_creacion,palabras_clave) values ((select max(id_u) from usuario),'" + tituloO + "','" + Descripcion + "','" + Ruta + "','" + Fecha + "','" + PClave + "')"
        probaMySQL.run_query(query)



    def obtenDir():
        global archivo
        extension = '*'
        archivo = eg.fileopenbox(msg="Subir OA",
                                 title="Control: filesavebox",
                                 default='',
                                 filetypes=extension)


    def obFecha():
        child = tk.Toplevel()
        calendario = wCalendar.Calendar(child, fecha)

    def hola():
        global archivo
        nombreA = eAutor.get()
        titulo=eNombre.get()
        institucion=eInsti.get()
        descrip=eDescrip.get()
        ruta=archivo
        fechaC=repr(fecha['year_selected'])+'/'+repr(fecha['month_selected'])+'/'+repr(fecha['day_selected'])
        pClave=eClave.get()
        print nombreA,titulo,institucion,descrip,ruta,fechaC,pClave
        guardarBase(institucion,nombreA,titulo,descrip,ruta,fechaC,pClave)

        # vista del catalogo



    def salir():
        ventana.destroy()

    ventana = tk.Toplevel()
    ventana.title("Subir Nuevo OA")
    # formato ventana
    ventana.geometry('250x300')
    ventana.configure(background='dark turquoise')

    etiqueta1 = tk.Label(ventana, text="Nombre", bg="blue", fg="white")
    etiqueta1.pack(fill=tk.X)

    eNombre = tk.Entry(ventana)
    eNombre.pack(fill=tk.X)

    etiqueta2 = tk.Label(ventana, text="Descripción", bg="blue", fg="white")
    etiqueta2.pack(fill=tk.X)

    eDescrip = tk.Entry(ventana)
    eDescrip.pack(fill=tk.X)

    etiqueta3 = tk.Label(ventana, text="Autor", bg="blue", fg="white")
    etiqueta3.pack(fill=tk.X)

    eAutor = tk.Entry(ventana)
    eAutor.pack(fill=tk.X)

    etiqueta5 = tk.Label(ventana, text="Institucion", bg="blue", fg="white")
    etiqueta5.pack(fill=tk.X)

    eInsti = tk.Entry(ventana)
    eInsti.pack(fill=tk.X)

    btnFecha=tk.Button(ventana, text="Fecha Creacion", fg="blue", command=obFecha)
    btnFecha.pack()

    etiqueta4 = tk.Label(ventana, text="palabras clave", bg="blue", fg="white")
    etiqueta4.pack(fill=tk.X)

    eClave = tk.Entry(ventana)
    eClave.pack(fill=tk.X)

    btnarchivo= tk.Button(ventana, text="seleccionar archivo", fg="blue", command=obtenDir)
    btnarchivo.pack()

    btnGuardar = tk.Button(ventana, text="subir", fg="blue", command=hola)
    btnGuardar.pack(side=tk.LEFT)

    btnSalir = tk.Button(ventana, text="cancelar", fg="blue", command=salir)
    btnSalir.pack(side=tk.RIGHT)

    #ventana.mainloop()


"""
self.some_list = [ 'ADDRESS BOOK' ] 
db = MySQLdb.connect("localhost",port=3306, user="root", passwd="mysql", db="compudist" ) 
cursor = db.cursor() 
cursor.execute("SELECT usuario FROM logservi") 
db.commit() 
numrows = int(cursor.rowcount) 
for i in range(0,numrows): 
    row = cursor.fetchone() 
    if (row): 
        self.some_list.append(row[0])
"""

"""
  combo=ttk.Combobox(ventana, state='normal')
listaa=[1,2,3]
combo["values"]=listaa
combo.set("escoge una")
combo.bind("<<ComboboxSelected>>", hola)
combo.pack()  
"""