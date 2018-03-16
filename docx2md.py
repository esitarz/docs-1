# python file to pandoc a whole director


# pandoc -f docx -t markdown "Add Quantity Multiplier to a Product.docx" -o "AddQuantityMultiplierToProduct.md"




import subprocess
from subprocess import Popen, PIPE, STDOUT
import sys
import re
import os


# Popen pandoc shell command
#p = Popen(['pandoc', '-f', 'markdown', '-t', 'latex', '--wrap=preserve'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)


# get folder to convert

input = '/docs/content/copies/1_Use_Case_Guides/1_Product_Catalog_Management/'


# get list of docx files in folder

files = os.listdir(input)

#print(files)

for file in files:
	if "docx" in file:
		docx = '"'+input+file+'"'
		mdOut = '"'+input+os.path.splitext(file)[0]+'.md"'
		print('pandoc -f docx -t markdown '+docx+' -o '+mdOut+' --extract-media='+input+'images/ -s \n')
		Popen(['pandoc', '-f', 'docx', '-t', 'markdown', docx, '-o '+mdOut])
	else:
		continue