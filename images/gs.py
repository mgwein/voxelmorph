# -*- coding: utf-8 -*-
"""
File:   gs_crop.py
Author: MATT WEIN
Date:   11/1/2021
Desc:   Converts sample images to greyscale and resizes to 150 x 150
    
"""

import cv2
import glob

for filename in glob.glob(r'images\sa_orig\*.png'):
    print(filename)
    img=cv2.imread(filename) 
    rl=cv2.resize(img, (32,32))
    gray_image = cv2.cvtColor(rl, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'{filename}.gs.png', gray_image)