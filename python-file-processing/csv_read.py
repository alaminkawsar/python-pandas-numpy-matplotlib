import os
import csv
from matplotlib.pyplot import axis
import pandas as pd
path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/python-file-processing'

mask = {'file1/imageName':1, 'file2/imageName':1}
mask['file3/imageName']=1

new_list = []
with open(os.path.join(path,'dataset.csv'), 'r') as file:
    read = csv.reader(file)
    for row in read:
        if row[0] not in mask.keys():
            #writer.writerow(row)
            new_list.append(row)

with open(os.path.join(path,'dataset.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_list)
print(new_list)