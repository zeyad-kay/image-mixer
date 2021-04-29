import tkinter as tk
from Output_Panel import Output_Panel
from Input_Panel import Input_Panel
from lib import MenuBar
from Mixer import Mixer

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
        
        input1 = self.create_input_panel("snake2.jpeg")
        input1.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        
        input2 = self.create_input_panel("snake1.jpeg")
        input2.grid(row=1,column=0,sticky="nsew",padx=4,pady=4)
        
        output = self.create_output_panel()
        output.grid(row=1,column=1,sticky="nsew",padx=4,pady=4)
        
        mixer = self.create_mixer_panel(input1,input2,output)
        mixer.grid(row=0,column=1,sticky="nsew",padx=4,pady=4)
    
    def create_input_panel(self,image):
        panel=Input_Panel(self,image)
        return panel

    def create_mixer_panel(self,input1,input2,output):
        mixer = Mixer(self,input1.image,input2.image,output.image1,output.image2)
        return mixer
    
    def create_output_panel(self):
        panel=Output_Panel(self)
        return panel

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root,title="Image Viewer")
    app.mainloop()