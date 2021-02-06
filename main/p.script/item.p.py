import tkinter as tk
from tkinter import ttk
from tkinter import *

master = Tk()
master.title('CIT Generator - Items')
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

n = tk.StringVar() 
typeString = ttk.Combobox(master, width=18, textvariable=n) 
typeString['values'] = ('item', 'enchantment', 'armor', 'elytra') 
typeString.grid(column = 1, row = 2) 
typeString.current()

m = tk.StringVar() 
itemString = ttk.Combobox(master, width=18, textvariable=m) 
itemString['values'] = ('minecraft:acacia_door', 'minecraft:acacia_fence', 'minecraft:acacia_fence_gate', 'minecraft:acacia_stars',
                    'minecraft:activator_rail', 'minecraft:air', 'minecraft:anvil', 'minecraft:apple', 'minecraft:armor_stand',
                    'minecraft:arrow', 'minecraft:baked_potato', 'minecraft:banner', 'minecraft:barrier', 'minecraft:beacon',
                    'minecraft:bed', 'minecraft:bedrock', 'minecraft:beef', 'minecraft:birch_door') 
itemString.grid(column = 1, row = 3) 
itemString.current() 

typeText = Label(master, text='Type')
itemText = Label(master, text='Item')
imageText = Label(master, text='Image [.png]')

imageString = tk.Entry(master)
modelString = tk.Entry(master)
loreString = tk.Entry(master)
itemTitleString = tk.Entry(master)
identString = tk.Entry(master)
weightString = tk.Entry(master)

typeText.grid(row=2, column=0, sticky=W)
itemText.grid(row=3, column=0, sticky=W)
imageText.grid(row=4, column=0, sticky=W)

imageString.grid(row=4, column=1)
modelString.grid(row=5, column=1)
loreString.grid(row=6, column=1)
itemTitleString.grid(row=7, column=1)
identString.grid(row=8, column=1)
weightString.grid(row=9, column=1)

model = IntVar()
Checkbutton(master, text="Model [.json]", variable=model).grid(row=5, sticky=W)
lore = IntVar()
Checkbutton(master, text="Item Lore", variable=lore).grid(row=6, sticky=W)
itemTitle = IntVar()
Checkbutton(master, text="Item Name", variable=itemTitle).grid(row=7, sticky=W)
ident = IntVar()
Checkbutton(master, text="Item ID", variable=ident).grid(row=8, sticky=W)
weight = IntVar()
Checkbutton(master, text="Item Weight", variable=weight).grid(row=9, sticky=W)

image_name = ''
model_name = ''
lore_name = ''


def fetchData():
    print('fetching data...')
    image_name = imageString.get()
    item_type = typeString.get()
    item_name = itemString.get()
    print(f'Image Name: >{image_name}<')
    print(f'Item Type Name: >{item_type}<')
    print(f'Item Name: >{item_name}<')

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
            propertyFile = open(f'{image_name.replace(".png", ".properties")}', 'w')
            print('Created without ".png"')
        else:
            propertyFile = open(f'{image_name}.properties', 'w')
            print('Created')

        propertyFile.write(f'type={item_type}\n')
        propertyFile.write(f'items={item_name}\n')
        propertyFile.write(f'texture=./{image_name}\n')

        if model.get() == 1:
            propertyFile.write(f'model=./{model_name}\n')
        if lore.get() == 1:
            propertyFile.write(f'nbt.display.Lore.*=ipattern:*{lore_name}*\n')
        if itemTitle.get() == 1:
            propertyFile.write(f'nbt.display.Name=ipattern:*{item_name}*\n')
        if ident.get() == 1:
            propertyFile.write(f'nbt.EtraAttributes.id={item_id}\n')
        propertyFile.close()
        print('Success')
    except:
        print('Error while creating file, look for:\n- blank name\n- duplicate file')

compileBtn = tk.Button(master, text='Create File', command=fetchData)
compileBtn.grid(row=10, column=0, sticky=W)

master.mainloop()