from .Combobox import Combobox
from .Component_Control import Component_Control
import tkinter as tk

class Mixer(tk.Frame):
    def __init__(self,master,input_image1,input_image2,output_image1,output_image2):
        super().__init__(master,background="white",border=1,relief="solid")
        self.master = master
        self.outputs_controls = {
            "Output 1": None,
            "Output 2": None
        }
        self.modes = ("Magnitude","Phase","Real","Imaginary","UniMagnitude","UniPhase")
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
          
        self.output_cbox = Combobox(self,values=["Output 1","Output 2"])
        self.output_cbox.set(self.output_cbox["values"][0])
        self.output_cbox.grid(row=0,column=0,sticky="ns",padx=4,pady=4)
        self.output_cbox.on_change(self.switch_outputs)

        for i in range(2):
            components_container = tk.Frame(self,bg="white")
            components_container.rowconfigure(0,weight=1)
            components_container.rowconfigure(1,weight=1)
            components_container.columnconfigure(0,weight=1)
            components_container.grid(row=1,column=0,sticky="nsew")

            comp1 = Component_Control(components_container,"Component 1",input_image1,input_image2,output_image1,output_image2,bg="white")
            comp2 = Component_Control(components_container,"Component 2",input_image1,input_image2,output_image1,output_image2,bg="white")
            comp1.component_cbox["values"] = self.modes
            comp1.component_cbox.set("Magnitude")
            comp1.update_cbox_choices("Magnitude")
            comp1.grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
            comp2.grid(row=1,column=0,sticky="nsew",padx=4,pady=4)
            self.outputs_controls["Output " + str(i+1)] = components_container
        
        self.switch_outputs("Output 1")

    def switch_outputs(self,label):
        # Put selected output on top of the other
        self.outputs_controls[label].lift()