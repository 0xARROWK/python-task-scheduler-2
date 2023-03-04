from tkinter import *
from tkinter import ttk
from model import *


class Gestion(Frame):
    def __init__(self, root, w, atelier, cb_add, cb_mod, cb_del):
        Frame.__init__(self, root)
        self.width = w
        self.atelier = atelier
        # création du tableau, affichage, et on l'enregistre pour plus tard
        tableau = ttk.Treeview(self, selectmode="browse")
        tableau.pack(side=TOP, fill=BOTH, expand=True)
        self.tableau = tableau

    def display_array(self):
        # ajout les M+3 colonnes, avec des clefs pour accès
        self.tableau['columns'] = ['LBL'] + ["M" + str(j + 1) for j in range(0, self.atelier.machines_nb)] + ["Début", "Fin"]
        labels = ['Label'] + ["Temps sur M" + str(j + 1) for j in range(0, self.atelier.machines_nb)] + ["Début", "Fin"]
        for idx, column in enumerate(self.tableau['columns']):
            self.tableau.column(column, width=self.width // (self.atelier.machines_nb + 3))
            self.tableau.heading(column, text=labels[idx], anchor=CENTER)
        self.tableau.column("#0", width=0, stretch=NO)
        self.tableau.heading("#0", text="", anchor=CENTER)

    def fill_array(self):
        for i in self.tableau.get_children():
            self.tableau.delete(i)
        tasks_time = self.atelier.tasks_time()
        for i in range(0, len(self.atelier.tasks)):
            iid = self.atelier.tasks[i]['id']
            vals = [self.atelier.tasks[i]['label']]
            for j in range(0, self.atelier.machines_nb):
                vals.append(self.atelier.tasks[i]['p'][j])
            vals.append(tasks_time[i]['start'])
            vals.append(tasks_time[i]['end'])
            self.tableau.insert(parent='', index='end', iid=iid, values=vals)
