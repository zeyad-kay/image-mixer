import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Graph(tk.Frame):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self._figure = Figure(figsize=(4, 4), constrained_layout=True)
        FigureCanvasTkAgg(self._figure, master=self)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self._figure.canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')

    def plot(self,x,y):
        ax = self._figure.subplots(1,1)
        try:
            ax.plot(x,y)
        except Exception as e:
            print(e)
        finally:
            self._figure.canvas.draw_idle()
            self._figure.canvas.flush_events()