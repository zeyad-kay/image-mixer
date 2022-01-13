import tkinter as tk
import sys
from tkinter import filedialog


class MenuBar(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open File",  command=self.file_upload)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit",  command=self.quit)

    def file_upload(self):
        files = 0
        self.master.files = []
        while files != 2:
            filename = filedialog.askopenfilename(initialdir="/",
                                                  title="Select a File",
                                                  filetypes=(("JPG files",
                                                              "*.jpg*"),
                                                             ("PNG files",
                                                              "*.PNG"),
                                                             ("all files",
                                                              "*.*"))) or ""
            self.master.files.append(filename)
            files = files + 1
        
        self.master.event_generate("<<Fileupload>>")
    def quit(self):
        sys.exit(0)
