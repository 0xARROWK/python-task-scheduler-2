from tkinter import *
from model import *
from view.Gestion import *


class Window:
    def __init__(self, atelier):
        self.atelier = atelier
        root = Tk()
        root.option_add('*foreground', 'black')
        root.tk.call("source", "azure.tcl")
        root.tk.call("set_theme", "dark")
        tabControl = ttk.Notebook(root, width=1100, height=700)
        onglet1 = Gestion(tabControl, 1090, atelier, None, None, None)
        onglet1.display_array()
        onglet1.fill_array()
        onglet2 = Frame(tabControl)
        tabControl.add(onglet1, text='Gestion des tâches')
        tabControl.add(onglet2, text='Ordonnancement')
        tabControl.grid(row=2, column=0)

        # display window
        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
        x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
        y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
        root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))
        root.mainloop()

