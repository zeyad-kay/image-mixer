import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master,title):
        super().__init__(master)
        master.title(title)
        master.state("zoomed")

if __name__ == "__main__":
    app = Application(master=tk.Tk(),title="Image Viewer")
    app.mainloop()