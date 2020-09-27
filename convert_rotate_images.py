#!/usr/bin/python3

from PIL import Image
import os

INPUTDIR='./images'
OUTPUTDIR='/opt/icons'


for curDir, dirs, files in os.walk(INPUTDIR):
#  print(files)
  for file in files:
    filepath = os.path.join(curDir,file)
    outfilepath = os.path.join(OUTPUTDIR,file)

    try:
      img = Image.open(filepath)
      img = img.convert('L')
  
      #rotate 90, and reisize to 128x128
      img_rotate = img.rotate(90, expand=True)
      img_rotate_resize = img_rotate.resize((128,128))
  
      #save as jpeg
      img_rotate_resize.save(outfilepath,"JPEG")
    except Exception as e:
      print(e)
      
  
  break
