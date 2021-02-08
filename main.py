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
url4 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/p.script/armor.p.py'
armorSc = requests.get(url4)

def runItem():
    url1 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pysc/item.p.py'
    itemSc = requests.get(url1)
    exec(itemSc.text)
def runBow():
    url2 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pysc/bow.p.py'
    bowSc = requests.get(url2)
    exec(bowSc.text)
def runRod():
    url3 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pysc/rod.p.py'
    rodSc = requests.get(url3)
    exec(rodSc.text)
def runArmor():
    url4 = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pysc/armor.p.py'
    armorSc = requests.get(url4)
    exec(armorSc.text)

def runItemBeta():
    url1B = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/beta/p.script/item.p.py'
    itemScBeta = requests.get(url1B)
    exec(itemScBeta.text)
def runBowBeta():
    url2B = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/pybeta/p.scriptsc/bow.p.py'
    bowScBeta = requests.get(url2B)
    exec(bowScBeta.text)
def runRodBeta():
    url3B = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/beta/p.script/rod.p.py'
    rodScBeta = requests.get(url3B)
    exec(rodScBeta.text)
def runArmorBeta():
    url4B = 'https://raw.githubusercontent.com/stef-the/Auto-Properties/master/main/beta/p.script/armor.p.py'
    armorScBeta = requests.get(url4B)
    exec(armorScBeta.text)

def run():
    master = Tk()
    master.title('select mode')
    master.grid_rowconfigure(0, weight=1)
    master.grid_columnconfigure(0, weight=1)

    typeText = Label(master, text='Close')
    typeText.grid(row=2, column=1, sticky=E)

    beta = IntVar()
    Checkbutton(master, text="Use Beta", variable=beta).grid(row=2, column=3, sticky=W)

    if beta.get() == 0:
        itemBtn = tk.Button(master, text=' Item', command=runItem)
        itemBtn.grid(row=1, column=1, sticky=W)
        bowBtn = tk.Button(master, text=' Bow  ', command=runBow)
        bowBtn.grid(row=1, column=2, sticky=W)
        rodBtn = tk.Button(master, text=' Rod ', command=runRod)
        rodBtn.grid(row=1, column=3, sticky=W)
        armorBtn = tk.Button(master, text='Armor', command=runArmor)
        armorBtn.grid(row=1, column=4, sticky=W)
    
    elif beta.get() == 1:
        itemBtn = tk.Button(master, text=' Item', command=runItemBeta)
        itemBtn.grid(row=1, column=1, sticky=W)
        bowBtn = tk.Button(master, text=' Bow  ', command=runBowBeta)
        bowBtn.grid(row=1, column=2, sticky=W)
        rodBtn = tk.Button(master, text=' Rod ', command=runRodBeta)
        rodBtn.grid(row=1, column=3, sticky=W)
        armorBtn = tk.Button(master, text='Armor', command=runArmorBeta)
        armorBtn.grid(row=1, column=4, sticky=W)

    closeBtn = tk.Button(master, text='⌧', command=master.destroy)
    closeBtn.grid(row=2, column=2, sticky=W)


    master.mainloop()

run()