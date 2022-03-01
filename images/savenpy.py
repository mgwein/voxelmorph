# # -*- coding: utf-8 -*-
# """
# File:   img_nparray.py
# Author: MATT WEIN
# Date:   11/1/2021
# Desc:   Takes sample images and creates an array of the sampled images of shape=A,B,C (A = images, B = xscale, C = yscale)
#         and corresponding groundtruth numpy array with the appropriate labels for each image class
    
# """

# from PIL import Image
# import numpy as np
# import glob
# from matplotlib import pyplot as plt

# files = glob.glob('*.png')

# char_count = 20
# Labels = np.zeros([1,char_count])
# Images = np.zeros([char_count,512,512])

# for ind,val in enumerate(files):
#     im = Image.open(val)
#     dat = np.asarray(im)
#     Images[ind,:,:] = dat
#     Labels[0,ind] = int(ind)

# np.save('Imagesvx',Images)
# np.save('Labelsvx',Labels.astype(int))


# with open('Imagesvx.npy','rb') as f:
#     a = np.load(f)

# with open('Labelsvx.npy','rb') as f:
#     b = np.load(f)

# for i in range(char_count):
#     plt.imshow(a[i,:,:],cmap='gray')
#     plt.title(b[0,i])
#     plt.show()

from PIL import Image
import os, sys
import cv2
import numpy as np

'''
Converts all images in a directory to '.npy' format.
Use np.save and np.load to save and load the images.
Use it for training your neural networks in ML/DL projects. 
'''

# Path to image directory
path = "C:/Users/mgwei/Desktop/GitHub/voxelmorph/images/sa_resized/"
dirs = os.listdir( path )
dirs.sort()
x_train=[]

def load_dataset():
    # Append images to a list
    for item in dirs:
        if os.path.isfile(path+item):
            # im = Image.open(path+item).convert("GREY")
            im = Image.open(path+item)
            im = np.array(im)
            x_train.append(im)

if __name__ == "__main__":
    
    load_dataset()
    
    # Convert and save the list of images in '.npy' format
    imgset=np.array(x_train)
    np.save("imgds5.npy",imgset)