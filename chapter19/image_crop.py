#! python3
# program to crop screenshots of Mariczka's lectures
# usage: in CLI type python3 image_crop.py
# the images to crop need to be in the same folder as the program

from pathlib import Path
from PIL import Image
import os
 
p = Path.cwd()
os.makedirs('cropped_images')
s = Path.cwd() / 'cropped_images'

for file_obj in p.glob('*.png'):
	scr_im = Image.open(file_obj.name)
	crpscr_im = scr_im.crop((302, 194, 1616, 934))
	crpscr_im.save(s / file_obj.name)
