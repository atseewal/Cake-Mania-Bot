# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:04:50 2020

@author: atseewal
"""

"""
Surface Pro, not docked
-----------------------

Cake Mania is launched in windowed mode and the window is moved into the top left corner with the top bar still showing
Screen resolution is 1920x1080, scaling is set to 125%, and surface is not docked
x_pad = 0
y_pad = 32
play area = x_pad, y_pad, x_pad+998, y_pad+750
"""

# Globals
#--------
x_pad = 0
y_pad = 32

from PIL import ImageGrab
import os
import time
import win32api, win32con

def ScreenGrab():
    box = (x_pad, y_pad, x_pad+998, y_pad+750)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print('left click')

def mousePos(cord):
    win32api.SetCursorPos(x_pad + cord[0], y_pad + cord[1])

def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)

def main():
    pass

# Only run if it is run, not if imported
if __name__ == '__main__':
    main()