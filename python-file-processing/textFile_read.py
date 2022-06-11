import os
import csv
path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/python-file-processing'
with open(os.path.join(path,"text_file.txt"), "r") as f:
    for line in f.readlines():
        line = line[:-1]
        d = line.split(',')
        print(d)
