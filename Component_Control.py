import numpy as np
import threading
from lib import Slider,Combobox,Fourier
import tkinter as tk


class Component_Control(tk.Frame):
    def __init__(self, master, text, image1, image2, output_image1, output_image2, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.imgs = {
            "Img 1": image1,
            "Img 2": image2
        }
        self.outputs = {
            "Output 1": output_image1,
            "Output 2": output_image2
        }
        self.complex_components = {
            "Magnitude": Fourier.magnitude_gain,
            "Phase": Fourier.phase_gain,
            "Real": Fourier.real_gain,
            "Imaginary": Fourier.imaginary_gain,
            "UniMagnitude": Fourier.unimagnitude,
            "UniPhase": Fourier.uniphase,
        }

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        l = tk.Label(self, text=text, bg="white")
        l.grid(row=0, column=0)

        self.image_cbox = Combobox(self, values=["Img 1", "Img 2"])
        self.image_cbox.grid(row=0, column=1)

        self.component_cbox = Combobox(
            self, values=["Magnitude", "Phase", "Real", "Imaginary", "UniMaganitude", "UniPhase"])
        self.component_cbox.grid(row=0, column=2)

        self.factor_slider = Slider(
            self, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL)
        self.factor_slider.on_change(self.generate_output, lazy=True)
        self.factor_slider.grid(row=0, column=3)

    def generate_output(self, *args):
        t = threading.Thread(target=self.mix)
        t.start()

    def mix(self):
        current_output = self.master.master.output_cbox.get()
        output = 0
        for component in self.master.children.values():
            fourier = self.imgs[component.image_cbox.get()].get_fourier()
            factor = component.factor_slider.get() / 100
            output = output + self.complex_components[component.component_cbox.get()](fourier,factor)

        # changing the phase then applying inverse and real results in
        # -ve values???
        decimal_pixels = Fourier.real(Fourier.inverse(output))
        decimal_pixels = np.round(decimal_pixels).astype(np.uint32)
        self.outputs[current_output].set_image(decimal_pixels,self.imgs["Img 1"].size,rgb=False)
        self.outputs[current_output].show()