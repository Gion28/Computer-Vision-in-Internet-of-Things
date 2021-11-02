import tkinter
from tkinter import ttk

"""
Main Properties
"""
root = tkinter.Tk()
root.title("Image Matching")
root.geometry("0x0")

"""
Widgets Properties
"""
#Tabs
notebook = tkinter.ttk.Notebook(root)
notebook.add(tkinter.Frame(notebook), text="Week1")
notebook.add(tkinter.Frame(notebook), text="Week2")
notebook.add(tkinter.Frame(notebook), text="Week3")

#Widget inside tabs
algorithm = ttk.Combobox(notebook.nametowidget(notebook.tabs()[0]))
algorithm["values"] = ("test", "test2")
algorithm["state"] = "readonly"

"""
Widgets Functions
"""
def algorithm_selected(event):
    print(algorithm.get())

"""
Widget Functions Binding
"""
algorithm.bind("<<ComboboxSelected>>", algorithm_selected)

"""
Widget Packing
"""
notebook.pack(expand=True, fill=tkinter.BOTH)
algorithm.pack()

"""
Main Loop
"""
root.mainloop()