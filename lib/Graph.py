import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Graph(tk.Frame):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        px = 1/plt.rcParams['figure.dpi']
        
        self._figure = Figure(figsize=(3, 3), constrained_layout=True)
        self._figure.subplots(1,1)
        
        FigureCanvasTkAgg(self._figure, master=self)
        
        self._figure.canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')
    
    def plot(self,x,y):
        ax = self._figure.axes[0]
        ax.clear()
        try:
            ax.plot(x,y)
        except Exception as e:
            print(e)
        finally:
            self._figure.canvas.draw_idle()
            self._figure.canvas.flush_events()
    
    def image(self,data,cmap):
        ax = self._figure.axes[0]
        ax.clear()
        try:
            ax.imshow(data,cmap)
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        except Exception as e:
            print(e)
        finally:
            self._figure.canvas.draw_idle()
            self._figure.canvas.flush_events()