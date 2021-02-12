# Auto-Properties
Creates a .properties file for your Optifine CIT, based off of file input, to make texture packs a little easier to make. The script was built on **Python 3.8.2** and the GUI module used is **tkinter** (universally installed into python).

Started Feb. 5, 2021
### How do I use it?
- Choose what you want to make a file for

- Fill in the Text Boxes (ones without check marks are necessary for it to work)

- Check off boxes with extra info you would like to put in (model, item name, item ID, lore elements)

### What does it do?
- Item:
  - Input boxes for `type`, `item`, and `image`. 
  - Toggleable input boxes for `model`, `lore`, `item name`, and `item ID`.
  
- Bow:
  - Input boxes for bow frames (0, 1, 2)
  - Input box for standby bow
  - Toggleable input boxes for `model`, `lore`, `item name`, and `item ID`.
  
- Fishing Rod:
  - Input boxes for Cast/Uncast rod frames
  - Toggleable input boxes for `model`, `lore`, `item name`, and `item ID`.
  
- Armor: (WIP - DO NOT USE)
  - Input boxes for Layer 1 / Layer 2 of armor

- Creates a `.properties` file matching image name, with inputs incorporated into it.

## Support
- Contact `_stefthedoggo#1698` on discord

- Create an issue on GitHub

### Checklist
- Fill `item` dropdown for items

- Create online sourcing for dropdown libraries to reduce file size and make updates easier

- Improve UI formatting and color

- Add dark mode detection and themeing

- Start creating simple CTM maker (custom blocks)

- Start creating simple Model (.json) maker (held positions, gui positions, 3rd person)

- Make .mcmeta maker (animated textures)