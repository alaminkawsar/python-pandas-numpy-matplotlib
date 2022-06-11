import os
import csv
path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/python-file-processing'
list2d = []
indx = 0
with open(os.path.join(path,"text_file.txt"), "r") as f:
    for line in f.readlines():
        if line[-1]=='\n' :
            line = line[:-1] 
        new_val = line.split(',')
        list2d.append(new_val)

print(list2d)

with open(os.path.join(path,'dataset.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(list2d)
    