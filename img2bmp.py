##########################
# How to use this script #
##########################
#
# Run without arguments or:
#
# General:
# img2bmp.py "filename or path" "number of colors"
#
# For Example:
#
# Linux: 
# python3 img2bmp.py "/path/to/file/image.jpg" 26 
#
# Windows:
# py img2bmp.py "C:/path/to/file/image.jpg" 26

from PIL import Image
import sys

# ask for filename/path if not provided
if len(sys.argv) == 1:
    print ("File name or path:")
    filename = input()
else:
    filename = sys.argv[1]

# Import file
img = Image.open(filename)

# Ask for colors if not provided
if len(sys.argv) == 3:
    colors = sys.argv[2]
else:
    print ("Amount of colors:")
    colors = input()

newname = filename.split('.')[0] + ".bmp"
img = img.convert("RGB", palette = Image.ADAPTIVE, colors = int(colors))
img = img.convert("P", palette = Image.ADAPTIVE, colors = int(colors))
img.save(newname)