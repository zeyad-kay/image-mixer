from lib import Combobox
from Component_Control import Component_Control
import tkinter as tk

class Mixer(tk.Frame):
    def __init__(self,master):
        super().__init__(master,background="white",border=1,relief="solid")
        self.master = master

        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
        
        output_combobox = Combobox(self,values=["Output 1","Output 2"])
        output_combobox.grid(row=0,column=0,sticky="ns",padx=4,pady=4)
        output_combobox.on_change(print)

        components_container = tk.Frame(self,bg="white")
        components_container.rowconfigure(0,weight=1)
        components_container.rowconfigure(1,weight=1)
        components_container.columnconfigure(0,weight=1)
        components_container.grid(row=1,column=0,sticky="nsew")

        comp1 = Component_Control(components_container,bg="white",text="Component 1")
        comp2 = Component_Control(components_container,bg="white",text="Component 2")
        comp1.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        comp2.grid(row=1,column=0,sticky="nsew",padx=4,pady=4)