#!/usr/bin/env python
#This program uses 3rd Plugin: Pillow ,Python Imaging Library
#
#Get color from an image

from PIL import ImageColor
import pyautogui

#1.Get RGBA from a color
print('Input color:')
colorName = input()
output = ImageColor.getcolor(colorName,'RGBA')
print('RGBA of '+ colorName +' color is :'+ str(output))

#2.Display the mouse cursor's current pipxel color
im = pyautogui.screenshot()
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print('Display the mouse cursor\'s current pipxel color.')
print('Press Ctrl-C to quit.')
try:
    while True:
        #TODO: Get and print the mouse coordinates.
        x,y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        pipxelColor = im.getpixel((x,y))
        r = str(pipxelColor[0])
        g = str(pipxelColor[1])
        b = str(pipxelColor[2])
        positionStr += ' RGB: (' + r.rjust(3)
        positionStr += ',' + g.rjust(3)
        positionStr += ',' + b.rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')

#3.Get RGBA from an image and it's coordinates
#TODO: