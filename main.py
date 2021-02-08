import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests

url1 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/p.script/item.p.py'
itemSc = requests.get(url1)
url2 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/p.script/bow.p.py'
bowSc = requests.get(url2)
url3 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/p.script/rod.p.py'
rodSc = requests.get(url3)
url4 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/p.script/rod.p.py'
armorSc = requests.get(url4)

def runItem():
    exec(itemSc.text)
def runBow():
    exec(bowSc.text)
def runRod():
    exec(rodSc.text)
def runArmor():
    exec('print("pog")')

master = Tk()
master.title('select mode')
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

itemBtn = tk.Button(master, text='Item', command=runItem)
itemBtn.grid(row=1, column=1, sticky=W)
bowBtn = tk.Button(master, text='Bow', command=runBow)
bowBtn.grid(row=1, column=2, sticky=W)

rodBtn = tk.Button(master, text='Rod', command=runRod)
rodBtn.grid(row=2, column=1, sticky=W)
armorBtn = tk.Button(master, text='Armor', command=runArmor)
armorBtn.grid(row=2, column=2, sticky=W)

master.mainloop()