import tkinter as tk
from tkinter import *

master = Tk()
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

titleText = Label(master, text="CIT - Generator", font='Helvetica 15 bold')
typeText = Label(master, text='Type')
itemText = Label(master, text='Item')
imageText = Label(master, text='Image [.png]')
tk.Label(master).grid(row=2)
tk.Label(master).grid(row=3)
tk.Label(master).grid(row=5)

typeString = tk.Entry(master)
itemString = tk.Entry(master)
imageString = tk.Entry(master)
modelString = tk.Entry(master)
loreString = tk.Entry(master)

titleText.grid(row=1, column=0, sticky=W)
typeText.grid(row=2, column=0, sticky=W)
itemText.grid(row=3, column=0, sticky=W)
imageText.grid(row=4, column=0, sticky=W)


typeString.grid(row=2, column=1)
itemString.grid(row=3, column=1)
imageString.grid(row=4, column=1)
modelString.grid(row=5, column=1)
loreString.grid(row=6, column=1)

model = IntVar()
Checkbutton(master, text="Model [.json]", variable=model).grid(row=5, sticky=W)
lore = IntVar()
Checkbutton(master, text="Lore", variable=lore).grid(row=6, sticky=W)

image_name = ''
model_name = ''
lore_name = ''


def fetchData():
    print('fetching data...')
    image_name = imageString.get()
    print(f'Image Name: >{image_name}<')
    if model.get() == 1:
        model_name = modelString.get()
        print(f'Model Name: >{model_name}<')
    if lore.get == 1:
        lore_name = loreString.get()
        print(f'Lore: >{lore_name}<')
    print('data fetched')
    print('starting file creation')
    try:
        propertyFile = open(f'{image_name.replace(".png", ".properties")}', 'w')
        propertyFile.write('pog')
        propertyFile.close()
        print('Success')
    except:
        print('Error while creating file: Try again')

compileBtn = tk.Button(master, text='Compile File', command=fetchData)
compileBtn.grid(row=6, column=0, sticky=W)

master.mainloop()