import numpy as np
import threading
from .Slider import Slider
from .Combobox import Combobox
from core import Fourier
import tkinter as tk

class Component_Control(tk.Frame):
    def __init__(self, master, text, image1, image2, output_image1, output_image2, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.current_mix = 0
        self.imgs = {
            "Img 1": image1,
            "Img 2": image2
        }
        self.outputs = {
            "Output 1": output_image1,
            "Output 2": output_image2
        }

        self.complex_combinations = {
            "UniMagnitude": ["Phase","UniPhase"],
            "Magnitude": ["Phase","UniPhase"],
            "UniPhase": ["Magnitude","UniMagnitude"],
            "Phase": ["Magnitude","UniMagnitude"],
            "Real": ["Imaginary"],
            "Imaginary": ["Real"]
        }

        self.mode = {
            "Magnitude": Fourier.magnitude,
            "Phase": Fourier.phase,
            "Real": Fourier.real,
            "Imaginary": Fourier.imaginary,
            "UniMagnitude": Fourier.unimagnitude,
            "UniPhase": Fourier.uniphase,
        }

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.label = tk.Label(self, text=text, bg="white")
        self.label.grid(row=0, column=0)

        self.image_cbox = Combobox(self, values=["Img 1", "Img 2"])
        self.image_cbox.on_change(self.generate_output)
        self.image_cbox.set(self.image_cbox["values"][0])
        self.image_cbox.grid(row=0, column=1)

        self.component_cbox = Combobox(self)
        self.component_cbox.on_change(self.update_cbox_choices)
        self.component_cbox.grid(row=0, column=2)

        self.factor_slider = Slider(
            self, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL)
        self.factor_slider.on_change(self.generate_output, lazy=True)
        self.factor_slider.grid(row=0, column=3)

    def generate_output(self, *args):
        t = threading.Thread(target=self.mix)
        t.start()

    def update_cbox_choices(self,label):
        secondary_component = self.master.children["!component_control2"]
        if secondary_component is not self:
            secondary_component.component_cbox["values"] = self.complex_combinations[label]
            secondary_component.component_cbox.set(self.complex_combinations[label][0])
        self.generate_output()

    def get_mixed_component(self,component):
        factor = component.factor_slider.get() / 100
        fourier = component.imgs[component.image_cbox.get()].get_fourier()
        other_image_fourier = [img.get_fourier() for img in component.imgs.values() if img is not component.imgs[component.image_cbox.get()]][0]
        comp1_mode = component.mode[component.component_cbox.get()]
        return comp1_mode(fourier) * factor + comp1_mode(other_image_fourier) * (1-factor)

    def mix(self):
        current_output = self.master.master.output_cbox.get()
                    
        for component in self.master.children.values():
            if component is not self:
                other_component = component
        
        
        mix1 = self.get_mixed_component(self)
        mix2 = self.get_mixed_component(other_component)

        if self.component_cbox.get() == "UniPhase":
            mix1 = 0
        if self.component_cbox.get() == "UniMagnitude":
            mix1 = 1
        if self.component_cbox.get() == "Real":
            output = mix1 + mix2*1j
        elif self.component_cbox.get() == "Imaginary":
            output = mix1*1j + mix2
        elif self.component_cbox.get() == "Phase" or self.component_cbox.get() == "UniPhase":
            output = mix2 * np.exp(mix1*1j)
        else:
            output = mix1 * np.exp(mix2*1j)

        new_img = Fourier.real(Fourier.inverse2d(output))
        new_img = np.round(new_img).astype(np.uint8)
        self.outputs[current_output].set_image(new_img)
        self.outputs[current_output].show()