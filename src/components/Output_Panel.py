import tkinter as tk
from .Image import Image

class Output_Panel(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)

        self.image1 = Image(self)
        self.image2 = Image(self)
        self.image1.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        self.image2.grid(row=0,column=1,sticky="nsew",padx=4,pady=4)