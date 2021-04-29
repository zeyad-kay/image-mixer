from lib.Fourier import Fourier
from helpers import rgb_to_decimal,decimal_to_rgb
import tkinter as tk
from PIL import Image as PILImage
from PIL import ImageTk
import numpy as np

class Image(tk.Frame):
        def __init__(self,master,**kwargs):
            super().__init__(master,**kwargs)
            self.master = master
            self._image = None
            self._image_data = None
            self.fourier = None

            self.rowconfigure(0,weight=1)
            self.columnconfigure(0,weight=1)

        def show(self):           
            self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
            resize = self._image.resize((400,400),PILImage.ANTIALIAS)
            self.render = ImageTk.PhotoImage(resize)

            self.canvas.create_image(0, 0, image=self.render, anchor="nw", tags="IMG")
            self.canvas.grid(row=0,column=0,sticky="wens")

        def open_image(self,image):
            self._image = PILImage.open(image)
            self.size = self._image.size
            self._image_data = np.array(self._image.getdata())

        def set_image(self,data,size,rgb=True):
            if not rgb:
                data = decimal_to_rgb(data).reshape((size[1],size[0],3))
                # data = data.reshape((size[1],size[0]))
            self._image = PILImage.fromarray(data)
            self.size = self._image.size
            self._image_data = data

        def get_data(self,rgb=True):
            if rgb:
                return self._image_data
            else:
                return rgb_to_decimal(self._image_data)
        
        def get_fourier(self):
            if self.fourier is None:
                self.fourier = Fourier.fast(self.get_data(rgb=False))
            return self.fourier