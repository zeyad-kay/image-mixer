from .Graph import Graph
from core import Fourier
import tkinter as tk
from PIL import Image as PILImage
from PIL import ImageOps
import numpy as np

class Image(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self._image = None
        self._image_data = None
        self._fourier = None
        self._gray_scale = None
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.canvas = Graph(self)

    def show(self):           
        self.canvas.image(self.get_data(),'gray')
        self.canvas.grid(row=0,column=0,sticky="wens")

    def open_image(self,image):
        self._image = PILImage.open(image)
        self.size = self._image.size
        self._image_data = np.array(self._image)

    def set_image(self,data):
        self._image = PILImage.fromarray(data)
        self._image_data = data
        self._fourier = None

    def get_data(self):
        return self._image_data
        
    def get_fourier(self):
        if self._fourier is None:
            self._fourier = Fourier.fast2d(self.get_data())
        return self._fourier
    
    def get_gray(self):
        if self._gray_scale is None:
            self._gray_scale = ImageOps.grayscale(self._image)
        return self._gray_scale