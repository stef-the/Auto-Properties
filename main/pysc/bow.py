import tkinter as tk
from tkinter import ttk
from tkinter import *

master = Tk()
master.title('CIT Generator - Bow')
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

bowText0 = Label(master, text='Standby')
bowText1 = Label(master, text='Frame 1')
bowText2 = Label(master, text='Frame 2')
bowText3 = Label(master, text='Frame 3')

bowString0 = tk.Entry(master)
bowString1 = tk.Entry(master)
bowString2 = tk.Entry(master)
bowString3 = tk.Entry(master)

modelString = tk.Entry(master)
loreString = tk.Entry(master)
itemTitleString = tk.Entry(master)
identString = tk.Entry(master)
weightString = tk.Entry(master)

bowText0.grid(row=0, column=0, sticky=W)
bowText1.grid(row=1, column=0, sticky=W)
bowText2.grid(row=2, column=0, sticky=W)
bowText3.grid(row=3, column=0, sticky=W)

bowString0.grid(row=0, column=1)
bowString1.grid(row=1, column=1)
bowString2.grid(row=2, column=1)
bowString3.grid(row=3, column=1)

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

image_name_0 = ''
image_name_1 = ''
image_name_2 = ''
image_name_3 = ''
model_name = ''
lore_name = ''


def compileData():
    print('fetching data...')
    image_name_0 = bowString0.get()
    image_name_1 = bowString1.get()
    image_name_2 = bowString2.get()
    image_name_3 = bowString3.get()

    print(f'Standby Name: >{image_name_0}<')
    print(f'Frame 1 Name: >{image_name_1}<')
    print(f'Frame 2 Name: >{image_name_2}<')
    print(f'Frame 3 Name: >{image_name_3}<')
    print(f'Item Type Name: >item<')
    print(f'Item Name: >minecraft:bow<')

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
        if '.png' in image_name_0:
            propertyFile = open(f'{image_name_0.replace(".png", ".properties")}', 'w')
            print('Created without ".png"')
        else:
            propertyFile = open(f'{image_name_0}.properties', 'w')
            image_name_0 += '.png'
            print('Created')
        
        if not '.png' in image_name_1:
            image_name_1 += '.png'
        if not '.png' in image_name_2:
            image_name_2 += '.png'
        if not '.png' in image_name_3:
            image_name_3 += '.png'


        propertyFile.write(f'type=item\n')
        propertyFile.write(f'items=minecraft:bow\n')
        propertyFile.write(f'texture.bow_standby=./{image_name_0}\n')
        propertyFile.write(f'texture.bow_pulling_0=./{image_name_1}\n')
        propertyFile.write(f'texture.bow_pulling_1=./{image_name_2}\n')
        propertyFile.write(f'texture.bow_pulling_2=./{image_name_3}\n')

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
        print('Error while creating file, look for:\n- blank name\n- duplicate file\n- strange or duplicate naming')

compileBtn = tk.Button(master, text='Create File', command=compileData)
compileBtn.grid(row=9, column=0, sticky=W)
closeBtn = tk.Button(master, text='⌧', command=master.destroy)
closeBtn.grid(row=9, column=1, sticky=W)

master.mainloop()