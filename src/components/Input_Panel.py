import numpy as np
from core import Fourier
import tkinter as tk
from .Combobox import Combobox
from .Image import Image

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

        self.cbox = Combobox(self,values=["Magnitude","Phase","Real","Imaginary"])
        self.cbox.set(self.cbox["values"][0])
        self.cbox.grid(row=0,column=0,sticky="ns",padx=4,pady=4)
        self.cbox.on_change(self.update_image)

        imgs_container = tk.Frame(self,bg="white")
        imgs_container.rowconfigure(0,weight=1)
        imgs_container.columnconfigure(0,weight=1)
        imgs_container.columnconfigure(1,weight=1)

        # buggy!!!!
        self.image = Image(imgs_container)
        self.image.open_image(image)
        self.image.show()

        self.gray_fourier = Fourier.fast2d(self.image.get_gray())
        
        self.image2 = Image(imgs_container)
        self.image2.size = self.image.size
        self.update_image(self.cbox.get())

        self.image.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        self.image2.grid(row=0,column=1,sticky="nsew",padx=4,pady=4)
        imgs_container.grid(row=1,column=0,sticky="nsew",padx=4,pady=4)

    def update_image(self,label):
        # shift the fourier transform to the center
        # Without shifting the edges will illuminate instead
        # of the center
        if label == "Phase" or label == "Magnitude":
            shifted_fourier = np.fft.fftshift(self.gray_fourier)
            result = self.options.get(label)(shifted_fourier)
        else:
            result = self.options.get(label)(self.gray_fourier)
        
        if label == "Real":
            result =  np.nan_to_num(20*np.log(result)) + 20*np.log(np.abs(np.min(result)))
        
        if label == "Magnitude":
            result = 20*np.log(result)
            
        self.image2.set_image(result)
        self.image2.show()