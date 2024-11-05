from tkinter import ttk 
from tkinter import ttk
import tkinter as tk 

class SitenameFrame(ttk.Frame):
   
    def __init__(self,master=None,sitenames:list[str]=[],**kwargs):
        super().__init__(master=master, **kwargs)
        
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        for idx,value in enumerate(sitenames):
            column = idx % 2
            index = int(idx / 2)
            print(idx,value)
            print(f'column:{column}')
            print(f'index:{index}')
            tk.Radiobutton(self, text=value, value=value, variable=selected_radio).grid(column=column,row=index,sticky='w')
            print("================")