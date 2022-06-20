import csv
import os
import ossaudiodev
import pandas as pd
path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/python-file-processing/dataset.csv'

df = pd.read_csv(path)
df['filename'] = 'imageName'
df['ymax'] = '0'
df['height'] = '680'
df.to_csv(path, index=False)