import tkinter as tk
from tkinter import simpledialog
from tkinter import *

master = Tk()

master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

topText = Label(master, text="CIT - Generator", font='Helvetica 15 bold')
typeText = Label(master, text='Type')
itemText = Label(master, text='Item')
imageText = Label(master, text='Image [.png]')

typeString = tk.Entry(master)
itemString = tk.Entry(master)
imageString = tk.Entry(master)
modelString = tk.Entry(master)
loreString = tk.Entry(master)
itemTitleString = tk.Entry(master)
identString = tk.Entry(master)

topText.grid(row=1, column=0, sticky=W)
typeText.grid(row=2, column=0, sticky=W)
itemText.grid(row=3, column=0, sticky=W)
imageText.grid(row=4, column=0, sticky=W)


typeString.grid(row=2, column=1)
itemString.grid(row=3, column=1)
imageString.grid(row=4, column=1)
modelString.grid(row=5, column=1)
loreString.grid(row=6, column=1)
itemTitleString.grid(row=7, column=1)
identString.grid(row=8, column=1)

model = IntVar()
Checkbutton(master, text="Model [.json]", variable=model).grid(row=5, sticky=W)
lore = IntVar()
Checkbutton(master, text="Lore", variable=lore).grid(row=6, sticky=W)
itemTitle = IntVar()
Checkbutton(master, text="Item Name", variable=itemTitle).grid(row=7, sticky=W)
ident = IntVar()
Checkbutton(master, text="Item ID", variable=ident).grid(row=8, sticky=W)

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

    elif lore.get() == 1:
        lore_name = loreString.get()
        print(f'Lore: >{lore_name}<')

    elif itemTitle.get() == 1:
        item_name = itemTitleString.get()
        print(f'Item Title: >{item_name}<')

    elif ident.get() == 1:
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

        propertyFile.write('pog')
        propertyFile.close()
        print('Success')
    except:
        print('Error while creating file, look for:\n- blank name\n- duplicate file')

compileBtn = tk.Button(master, text='Create File', command=fetchData)
compileBtn.grid(row=9, column=0, sticky=W)

master.mainloop()