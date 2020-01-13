# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:04:50 2020

@author: atseewal
"""

from PIL import ImageGrab
import os
import time

def ScreenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    
def main():
    ScreenGrab()

# Only run if it is run, not if imported
if __name__ == '__main__':
    main()