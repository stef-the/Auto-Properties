import tkinter as tk
from tkinter import *

master = Tk()
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

imageText = Label(master, text='Image [.png]')
tk.Label(master).grid(row=2)
tk.Label(master).grid(row=3)
tk.Label(master).grid(row=5)

imageString = tk.Entry(master)
modelString = tk.Entry(master)
loreString = tk.Entry(master)

imageText.grid(row=2, column=0)
imageString.grid(row=2, column=1)
modelString.grid(row=3, column=1)
loreString.grid(row=5, column=1)

model = IntVar()
Checkbutton(master, text="Model [.json]", variable=model).grid(row=3, sticky=W)
lore = IntVar()
Checkbutton(master, text="Lore", variable=lore).grid(row=5, sticky=W)

def fetchData():
    print('fetching data')
runBtn = tk.Button(master, text='pog', command = fetchData())

master.mainloop()