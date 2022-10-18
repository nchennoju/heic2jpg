from wand.image import Image
from wand.display import display
import os
from tkinter import filedialog as fd


directory = fd.askdirectory()

for fn in os.listdir(directory):
    if fn.lower().endswith(".heic"):
        with Image(filename=os.path.join(directory, fn)) as img:
            print('Converting %s...' % os.path.join(directory, fn))
            print(img.size)
            with img.clone() as i:
                i.save(filename="conv\\"+ fn[0:-5] + '.jpg')
