import numpy as np
import cv2
from PIL import Image

bayer = Image.open("bayer1.png")
print(bayer.size)

width, height = bayer.size

output_image = bayer.load()

for j in range(1, height - 1):
    for i in range(1, width - 1):
        R, G, B = bayer.getpixel((i,j))
        if i % 2 == 0 and j % 2 == 0:
            R = np.rint((bayer.getpixel((i + 1, j))[0] + bayer.getpixel((i - 1, j))[0]) / 2)
            G = bayer.getpixel((i, j))[1]
            B = np.rint((bayer.getpixel((i, j+1))[2] + bayer.getpixel((i, j-1))[2]) / 2)
            output_image[i, j] = (int(R), int(G), int(B))
        if i % 2 != 0 and j % 2 != 0:
            B = np.rint((bayer.getpixel((i + 1, j))[2] + bayer.getpixel((i - 1, j))[2]) / 2)
            G = bayer.getpixel((i, j))[1]
            R = np.rint((bayer.getpixel((i, j+1))[0] + bayer.getpixel((i, j-1))[0]) / 2)
            output_image[i, j] = (int(R), int(G), int(B))
        if i % 2 == 0 and j % 2 != 0:
            B = bayer.getpixel((i, j))[2]
            R = np.rint((bayer.getpixel((i+1, j+1))[0] + bayer.getpixel((i+1, j-1))[0] + bayer.getpixel((i - 1, j-1))[0] + bayer.getpixel((i - 1, j+1))[0]) / 4)
            G = np.rint((bayer.getpixel((i, j+1))[1] + bayer.getpixel((i, j-1))[1] + bayer.getpixel((i + 1, j))[1] + bayer.getpixel((i - 1, j))[1]) / 4)
            output_image[i, j] = (int(R), int(G), int(B))
        if i % 2 != 0 and j % 2 == 0:
            R = bayer.getpixel((i, j))[0]
            B = np.rint((bayer.getpixel((i + 1, j + 1))[2] + bayer.getpixel((i + 1, j - 1))[2] + bayer.getpixel((i - 1, j - 1))[2] + bayer.getpixel((i - 1, j + 1))[2]) / 4)
            G = np.rint((bayer.getpixel((i, j + 1))[1] + bayer.getpixel((i, j - 1))[1] + bayer.getpixel((i + 1, j))[1] + bayer.getpixel((i - 1, j))[1]) / 4)
            output_image[i, j] = (int(R), int(G), int(B))


bayer.save("demosaic.png")

im = cv2.imread('strus.bmp')
im2 = cv2.imread('demosaic.png')

dift = (im - im2)**2
cv2.imwrite('odej.png', dift)
