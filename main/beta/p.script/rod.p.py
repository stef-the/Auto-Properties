import tkinter as tk
from tkinter import ttk
from tkinter import *

master = Tk()
master.title('CIT Generator - Rods')
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)


castText = Label(master, text='Cast [.png]')
uncastText = Label(master, text='Uncast [.png')

castString = tk.Entry(master)
uncastString = tk.Entry(master)
modelString = tk.Entry(master)
loreString = tk.Entry(master)
itemTitleString = tk.Entry(master)
identString = tk.Entry(master)
weightString = tk.Entry(master)

castText.grid(row=2, column=0, sticky=W)
uncastText.grid(row=3, column=0, sticky=W)

castString.grid(row=2, column=1)
uncastString.grid(row=3, column=1)
modelString.grid(row=4, column=1)
loreString.grid(row=5, column=1)
itemTitleString.grid(row=6, column=1)
identString.grid(row=7, column=1)
weightString.grid(row=8, column=1)

model = IntVar()
Checkbutton(master, text="Model [.json]", variable=model).grid(row=4, sticky=W)
lore = IntVar()
Checkbutton(master, text="Item Lore", variable=lore).grid(row=5, sticky=W)
itemTitle = IntVar()
Checkbutton(master, text="Item Name", variable=itemTitle).grid(row=6, sticky=W)
ident = IntVar()
Checkbutton(master, text="Item ID", variable=ident).grid(row=7, sticky=W)
weight = IntVar()
Checkbutton(master, text="Item Weight", variable=weight).grid(row=8, sticky=W)

image_name = ''
model_name = ''
lore_name = ''


def fetchData():
    print('fetching data...')
    cast_name = castString.get()
    uncast_name = uncastString.get()
    print(f'Cast Texture Name: >{cast_name}<')
    print(f'Uncast Texture Name: >{uncast_name}<')
    print(f'Item Type Name: >item<')
    print(f'Item Name: >minecraft:fishing_rod<')

    if model.get() == 1:
        model_name = modelString.get()
        print(f'Model Name: >{model_name}<')

    if lore.get() == 1:
        lore_name = loreString.get()
        print(f'Lore: >{lore_name}<')

    if itemTitle.get() == 1:
        item_name = itemTitleString.get()
        print(f'Item Title: >{item_name}<')

    if ident.get() == 1:
        item_id = identString.get()
        print(f'Item ID: >{item_id}<')

    print('data fetched')
    print('Starting file creation...')
    
    try:
        if '.png' in image_name:
            propertyFile = open(f'{cast_name.replace(".png", ".properties")}', 'w')
            print('Created without ".png"')
        else:
            propertyFile = open(f'{cast_name}.properties', 'w')
            cast_name += '.png'
            print('Created')
        if not '.png' in  uncast_name:
            uncast_name += '.png'

        propertyFile.write(f'type=item\n')
        propertyFile.write(f'items=minecraft:fishing_rod\n')
        propertyFile.write(f'texture=./{cast_name}\n')
        propertyFile.write(f'texture.fishing_rod_cast=./{uncast_name}\n')

        if model.get() == 1:
            propertyFile.write(f'model=./{model_name}\n')
        if lore.get() == 1:
            propertyFile.write(f'nbt.display.Lore=ipattern:*{lore_name}*\n')
        if itemTitle.get() == 1:
            propertyFile.write(f'nbt.display.Name=ipattern:*{item_name}*\n')
        if ident.get() == 1:
            propertyFile.write(f'nbt.EtraAttributes.id={item_id}\n')
        propertyFile.close()
        print('Success')
    except:
        print('Error while creating file, look for:\n- blank name\n- duplicate file')

compileBtn = tk.Button(master, text='Create File', command=fetchData)
compileBtn.grid(row=9, column=0, sticky=W)
closeBtn = tk.Button(master, text='⌧', command=master.destroy)
closeBtn.grid(row=9, column=1, sticky=W)

master.mainloop()