import os
import csv
path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/python-file-processing'

with open(os.path.join(path,'dataset.csv'), 'r') as file:
    read = csv.reader(file)
    for row in read:
        print(row)
    