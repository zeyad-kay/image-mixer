import tkinter as tk

class Slider(tk.Scale):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        self.master = master

    def on_change(self,callback):
        self.bind("<ButtonRelease>",lambda e: callback(self.get()))