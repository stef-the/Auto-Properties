import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests

master = Tk()
master.title('select mode')
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

beta = IntVar()
Checkbutton(master, text="Beta", variable=beta).grid(row=2, column=1, sticky=E)

def runItem():
    if beta.get() == 0:
        url1 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pysc/item.py'
    elif beta.get() == 1:
        url1 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/beta/p.script/item.p.py'
    itemSc = requests.get(url1)
    exec(itemSc.text)
def runBow():
    if beta.get() == 0:
        url2 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pysc/bow.py'
    elif beta.get() == 1:
        url2 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/beta/p.script/bow.p.py'
    bowSc = requests.get(url2)
    exec(bowSc.text)
def runRod():
    if beta.get() == 0:
        url3 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pysc/rod.py'
    elif beta.get() == 1:
        url3 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/beta/p.script/rod.p.py'
    rodSc = requests.get(url3)
    exec(rodSc.text)
def runArmor():
    if beta.get() == 0:
        url4 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pysc/armor.py'
    elif beta.get() == 1:
        url4 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/beta/p.script/armor.p.py'
    armorSc = requests.get(url4)
    exec(armorSc.text)

itemBtn = tk.Button(master, text=' Item', command=runItem)
itemBtn.grid(row=1, column=1, sticky=W)
bowBtn = tk.Button(master, text=' Bow  ', command=runBow)
bowBtn.grid(row=1, column=2, sticky=W)
rodBtn = tk.Button(master, text=' Rod ', command=runRod)
rodBtn.grid(row=1, column=3, sticky=W)
armorBtn = tk.Button(master, text='Armor', command=runArmor)
armorBtn.grid(row=1, column=4, sticky=W)

closeBtn = tk.Button(master, text='⌧', command=master.destroy)
closeBtn.grid(row=2, column=4, sticky=E)

master.mainloop()