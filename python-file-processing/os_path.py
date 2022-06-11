import os
import random

print(os.path)

source_dir = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/python-file-processing'
dirs = [os.path.join(source_dir, dir) for dir in os.listdir(source_dir)]

#random.shuffle(dirs)
for i in range(len(dirs)):
    print(dirs[i])