from tkinter import messagebox

class Messagebox():
    @staticmethod    
    def info(title=None, message=None, **options):
        messagebox.showwarning(title, message, **options)
    
    @staticmethod    
    def error(title=None, message=None, **options):
        messagebox.showerror(title, message, **options)
    
    @staticmethod    
    def warn(title=None, message=None, **options):
        messagebox.showerror(title, message, **options)
    
    @staticmethod    
    def question(title=None, message=None, **options):
        messagebox.askquestion(title, message, **options)
    
    @staticmethod    
    def ok_or_cancel(title=None, message=None, **options):
        messagebox.askokcancel(title, message, **options)
    
    @staticmethod    
    def yes_or_no(title=None, message=None, **options):
        messagebox.askyesno(title, message, **options)
    
    @staticmethod    
    def yes_or_no_or_cancel(title=None, message=None, **options):
        messagebox.askyesnocancel(title, message, **options)
    
    @staticmethod    
    def retry_or_cancel(title=None, message=None, **options):
        messagebox.askretrycancel(title, message, **options)