# Driver function
import os
'''Walk throuh deep by recursion and find out path,directory,files in this directory'''
path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/python-file-processing'
if __name__ == "__main__":
    for (root,dirs,files) in os.walk(path, topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')