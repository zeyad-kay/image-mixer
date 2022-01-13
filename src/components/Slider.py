import tkinter as tk

class Slider(tk.Scale):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        self.master = master

    def on_change(self,callback,lazy=False):
        if lazy:
            self.bind("<ButtonRelease>",lambda e: callback(self.get()))
        else:
            self["command"] = callback