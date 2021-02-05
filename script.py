import tkinter as tk
from tkinter import *

master = Tk()
tk.Label(master).grid(row=1)
tk.Label(master).grid(row=3)

modelString = tk.Entry(master)
loreString = tk.Entry(master)

modelString.grid(row=1, column=0)
loreString.grid(row=3, column=0)


model = IntVar()
Checkbutton(master, text="Model", variable=model).grid(row=0, sticky=W)
lore = IntVar()
Checkbutton(master, text="Lore", variable=lore).grid(row=2, sticky=W)

master.mainloop()

