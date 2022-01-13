import tkinter as tk
import logging
from components import Output_Panel, Input_Panel, MenuBar, Messagebox, Mixer

class Application(tk.Frame):
    def __init__(self,master,title):
        super().__init__(master,bg="white")
        self.master = master
        self.master.title(title)
        self.master.state("zoomed")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.grid(sticky="nsew")
        
        self.master.config(menu=MenuBar(self))
        self.files = []
        self.bind("<<Fileupload>>",lambda e: self.create_widgets())
        logging.basicConfig(filename='app.log',level=logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Application started successfully")

    def create_widgets(self):

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        
        input1 = self.create_input_panel(self.files[0])
        
        input2 = self.create_input_panel(self.files[1])
        
        
        if input1.image.size == input2.image.size:
            output = self.create_output_panel()
            mixer = self.create_mixer_panel(input1,input2,output)
            
            input1.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
            input2.grid(row=1,column=0,sticky="nsew",padx=4,pady=4)
            output.grid(row=1,column=1,sticky="nsew",padx=4,pady=4)
            mixer.grid(row=0,column=1,sticky="nsew",padx=4,pady=4)
            logging.info("Images Uploaded successfully")
        else:
            Messagebox.error(message="Images are not the same size!")
            self.files = []
            input1.destroy()
            input2.destroy()
            logging.error("Different Images size")

    def create_input_panel(self,image):
        panel=Input_Panel(self,image,bg="white")
        return panel

    def create_mixer_panel(self,input1,input2,output):
        mixer = Mixer(self,input1.image,input2.image,output.image1,output.image2)
        return mixer
    
    def create_output_panel(self):
        panel = Output_Panel(self,bg="white")
        return panel

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root,title="Image Viewer")
    app.mainloop()