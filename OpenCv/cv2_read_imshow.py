import cv2

path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/OpenCv/geeks14.jpg'

# Using cv2.imread() method
image = cv2.imread(path)

# Displaying the image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destoryAllWindows()