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
            
            self.rowconfigure(0,weight=1)
            self.columnconfigure(0,weight=1)
            self.canvas = tk.Canvas(self,bg="green")
            self.canvas.grid(row=0,column=0,sticky="nsew")
        

#     c = tk.Canvas(root,bg="green")
#     c.grid(row=0,column=0,sticky="nsew")
#     image = Image.open("demo.jpg")
#     render = ImageTk.PhotoImage(image)
#     i=c.create_image(100,100,image=render)


        def set_image(self,image="demo.jpg"):
            self._image = PILImage.open(image)
            render = ImageTk.PhotoImage(self._image)
            i=self.canvas.create_image(100,100,image=render)
            self._image_data = np.array(self._image.getdata())
            # print(self._image_data)
            # self.canvas.create_text(0,0,text="asdkir")
        def get_image_data(self):
            return self._image_data