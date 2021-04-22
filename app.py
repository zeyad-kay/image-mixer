from lib import Graph,MenuBar,Image
from Mixer import Mixer
import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master,title):
        super().__init__(master,bg="white")
        self.master = master
        self.master.title(title)
        self.master.state("zoomed")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.grid(sticky="nsew")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.master.config(menu=MenuBar(self))

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        
        self.create_input_panel().grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        self.create_mixer_panel().grid(row=0,column=1,sticky="nsew",padx=4,pady=4)
        self.create_input_panel().grid(row=1,column=0,sticky="nsew",padx=4,pady=4)
        self.create_output_panel().grid(row=1,column=1,sticky="nsew",padx=4,pady=4)
    
    def create_input_panel(self):
        container=tk.Frame(self)
        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)
        container.columnconfigure(1,weight=1)

        image = Image(container)
        image.set_image("demo.jpg")
        graph = Graph(container)
        graph.plot(x=[1,2,3],y=[1,2,3])    
        image.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        graph.grid(row=0,column=1,sticky="nsew",padx=4,pady=4)
        return container

    def create_mixer_panel(self):
        mixer = Mixer(self)
        return mixer
    
    def create_output_panel(self):
        container=tk.Frame(self)
        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)
        container.columnconfigure(1,weight=1)

        image1_output = Image(container)
        image2_output = Image(container)
        image1_output.set_image("demo.jpg")
        image2_output.set_image("demo.jpg")
        image1_output.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        image2_output.grid(row=0,column=1,sticky="nsew",padx=4,pady=4)
        return container

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root,title="Image Viewer")
    app.mainloop()