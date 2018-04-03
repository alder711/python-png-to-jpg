#!/usr/bin/env python
from glob import glob 
import ntpath                                                          
from PIL import Image
import os

ntpath.basename("a/b/c")

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)



pngs = glob('./**/*.png', recursive=True)

for j in pngs:
	print("\n\n\n")
	png_path = os.path.split(j)[0]
	#print("[PNG_PATH] " + png_path)
	png_name = path_leaf(j)
	#print("[PNG] " + png_name)

	jpg_name = png_name.replace("png","jpg")
	#print("[JPG] " + jpg_name)
	jpg_name_path = png_path + "/" + jpg_name 
	#print("[JPG_PATH_NAME] " + jpg_name_path)
    
	png_name_path = png_path + "/" + png_name
	print("[PNG] Opening '" + png_name_path + "'")
	img_png = Image.open(png_name_path)
	print("[PNG] Converting '" + png_name_path + "'")
	img_jpg = img_png.convert('RGB')
	print("[PNG] Saving '" + jpg_name_path + "'")
	img_jpg.save(jpg_name_path)
	print("[PNG] Deleting old '" + png_name_path + "'")
	os.remove(png_name_path)


