import numpy as np
from lib import Fourier
import tkinter as tk
from lib import Combobox, Graph,Image

class Input_Panel(tk.Frame):
    def __init__(self,master,image,**kwargs):
        super().__init__(master,**kwargs)

        self.master = master
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)

        self.options = {
            "Magnitude": Fourier.magnitude,
            "Phase":Fourier.phase,
            "Real":Fourier.real,
            "Imaginary":Fourier.imaginary
        }
        # box_container = tk.Frame(self,bg="red")
        # box_container.rowconfigure(0,weight=1)
        # box_container.columnconfigure(0,weight=1)

        self.cbox = Combobox(self,values=["Magnitude","Phase","Real","Imaginary"])
        self.cbox.grid(row=0,column=0,sticky="ns",padx=4,pady=4)
        self.cbox.on_change(self.update_image)
        # box_container.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)

        imgs_container = tk.Frame(self)
        imgs_container.rowconfigure(0,weight=1)
        imgs_container.columnconfigure(0,weight=1)
        imgs_container.columnconfigure(1,weight=1)

        # buggy!!!!
        self.image = Image(imgs_container)
        self.image.open_image(image)
        self.image.show()

        self.complex_data = self.image.get_fourier()
        self.freq = Fourier.frequency(len(self.complex_data))

        self.image2 = Image(imgs_container)
        self.image2.size = self.image.size
        self.update_image(self.cbox.get())

        self.image.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        self.image2.grid(row=0,column=1,sticky="nsew",padx=4,pady=4)
        imgs_container.grid(row=1,column=0,sticky="nsew",padx=4,pady=4)

    def update_image(self,label):
        result = self.options.get(label)(self.complex_data)
        data = Fourier.real(Fourier.inverse(result))
        data = np.round(data).astype(np.uint32)
        self.image2.set_image(data,self.image2.size,rgb=False)
        self.image2.show()