import os

path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/python-file-processing/hi.py'

if os.path.exists('hi.py'):
    os.remove(path)
else:
    print("No file or directory exists")