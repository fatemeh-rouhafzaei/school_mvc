import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ClassCheckBoxView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.master = master


    def populate(self, class_list):
        # for row in self.tree.get_children():
        #     self.tree.delete(row)
        for class_property in class_list:
            print(class_property)
            op1 = ttk.Checkbutton(self.master, text=class_property[1], variable='op1')
            op1.pack(fill=X, pady=5)
