from PIL import Image
import os
import numpy as np
import glob

#######################################################
# files = glob.glob('images'+'/*.png')

# Labels = np.zeros([1,20])
# array_of_images = []

# for ind,val in enumerate(files):
#     im = Image.open(val)
#     dat = np.asarray(im)
#     array_of_images.append(dat)
# np.savez("all_images.npz",array_of_images)

#######################################################
files = glob.glob('images'+'/*.png')

Labels = np.zeros([1,20])
images = np.zeros([20,512,512])

for ind,val in enumerate(files):
    im = Image.open(val)
    dat = np.asarray(im)
    images[ind,:,:] = dat
np.savez("all_images_gs.npz",images)