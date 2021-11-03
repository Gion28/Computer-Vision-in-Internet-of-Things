import tkinter
from tkinter import ttk
from tkinter import font
import time

"""
Main Properties
"""
root = tkinter.Tk()
root.title("Image Matching")
root.geometry("800x600")
root.minsize(800,600)

"""
Widgets Properties
"""
#Tabs
tabs = tkinter.ttk.Notebook(root)
tabs.add(tkinter.Frame(tabs), text="Settings")
tabs.add(tkinter.Frame(tabs), text="Attendance")
tabs.add(tkinter.Frame(tabs), text="Registation")

#Widget inside tabs
label_curtime = tkinter.Label(root)

label_font_families = tkinter.Label(tabs.nametowidget(tabs.tabs()[0]), text="font-family :")

comboBox_curtime_font_families = ttk.Combobox(tabs.nametowidget(tabs.tabs()[0]))
comboBox_curtime_font_families["values"] = font.families()
comboBox_curtime_font_families["state"] = "readonly"
comboBox_curtime_font_families.current(19)

label_font_size = tkinter.Label(tabs.nametowidget(tabs.tabs()[0]), text="font-size :")

comboBox_curtime_font_size = ttk.Combobox(tabs.nametowidget(tabs.tabs()[0]))
comboBox_curtime_font_size["values"] = (24,36,48)
comboBox_curtime_font_size["state"] = "readonly"
comboBox_curtime_font_size.current(1)

"""
Widgets Functions
"""
def comboBox_curtime_font_selected(event):
    label_curtime["font"] = (comboBox_curtime_font_families.get(), comboBox_curtime_font_size.get())

def root_update():
    label_curtime["text"] = time.strftime("%H:%M:%S")
    root.after(1000, root_update)

"""
Widget Functions Binding
"""
comboBox_curtime_font_families.bind("<<ComboboxSelected>>", comboBox_curtime_font_selected)
comboBox_curtime_font_size.bind("<<ComboboxSelected>>", comboBox_curtime_font_selected)

"""
Widget Packing
"""
tabs.pack(expand=True, fill=tkinter.BOTH)
label_curtime.pack()
label_font_size.grid(row=0,column=0)
comboBox_curtime_font_size.grid(row=0,column=1)
label_font_families.grid(row=1,column=0)
comboBox_curtime_font_families.grid(row=1,column=1)

"""
Main Loop
"""
root_update()
root.mainloop()