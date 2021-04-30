#!/usr/bin/env python3

# Get color from an image
# This program uses 3rd Plugin: Pillow ,Python Imaging Library

# 1.Enter color, print RGBA values
from PIL import ImageColor
# ask for color
print('Input color:')
colorName = input()
output = ImageColor.getcolor(colorName,'RGBA')
print('RGBA of '+ colorName +' color is :'+ str(output))

# 2.