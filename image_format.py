
import sys
import os
import PIL
from PIL import Image
import math

imageName = sys.argv[1]
folderPath = sys.argv[2]
newFolderPath = sys.argv[3]

path = "./%s/" % folderPath
newpath = "./%s/" % newFolderPath
i = 0

for filename in os.listdir(path):
    src = path + filename 
    newname = imageName + str(i) + ".jpeg"
    dst = path + newname 
    i += 1

    os.rename(src, dst) 

for filename in os.listdir(path):
    if filename != ".DS_Store":
        try:
            img = Image.open(path + filename)
            bg = Image.open('white.jpeg')
            w, h = img.size
            bg = bg.resize((w, h), Image.ANTIALIAS)
            bg = bg.convert("RGBA")
            img = img.convert("RGBA")
            bg.paste(img, (0, 0), img)
            img = bg

            print(filename)
            img = img.resize((286, 286), Image.ANTIALIAS)
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            img = img.save(newpath + filename.split('.')[0]+'.png', format='png')
        except:
            continue
        # wperce = (basewidth / float(img.size[0]))
        #  hsize = int((float(img.size[1]) * float(wpercent)))
        #  img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        #  img.save('resized_image.jpg')

