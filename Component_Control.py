from lib import Slider
from lib import Combobox
import tkinter as tk

class Component_Control(tk.Frame):
    def __init__(self, master, text, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)

        l = tk.Label(self,text=text)
        l.grid(row=0,column=0)

        c1 = Combobox(self,values=["Img 1", "Img 2"])
        c1.on_change(print)
        c1.grid(row=0,column=1)

        c2 = Combobox(self,values=["Mag", "Phase", "Real", "Imag", "uniMag", "uniPhase"])
        c2.on_change(print)
        c2.grid(row=0,column=2)
        
        c3 = Slider(self,from_=0,to=100,resolution=1,orient=tk.HORIZONTAL)
        c3.on_change(print)
        c3.grid(row=0,column=3)

