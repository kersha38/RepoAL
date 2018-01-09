import Tkinter as tk
import ttk
import probaMySQL

child = tk.Tk()
child.title('catalogo')
catalogo = ttk.Treeview(child,)
catalogo.pack()
item=catalogo.insert("", tk.END, text="Elemento 1")
catalogo.insert(item, tk.END, text="Subelemento 1")