import cv2 as cv
import cv2
import matplotlib.pyplot as plt

path = '/home/kawsar/Desktop/Deep Learning/python-pandas-numpy-matplotlib/OpenCv/rose.png'

#unchanged
image = cv2.imread(path,cv2.IMREAD_COLOR)

print(image.shape)
image=image[:,:,:,0]


# Displaying the image
#plt.imshow(image)
#plt.show()
cv2.imshow('image',image)
cv2.waitKey(0)
