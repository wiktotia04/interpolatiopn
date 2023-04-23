import numpy as np
import cv2

im = cv2.imread('strus.bmp')
im = cv2.resize(im, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)
(height, width) = im.shape[:2]
(B, G, R) = cv2.split(im)

bayer = np.empty((height, width), np.uint8)
# striped slicing for this pattern:
#   G R
#   B G
bayer[0::2, 0::2] = G[0::2, 0::2]  # top left
bayer[0::2, 1::2] = R[0::2, 1::2]  # top right
bayer[1::2, 0::2] = B[1::2, 0::2]  # bottom left
bayer[1::2, 1::2] = G[1::2, 1::2]  # bottom right

bayer = cv2.cvtColor(bayer, cv2.COLOR_GRAY2BGR)  # Convert from Grayscale to BGR (r=g=b for each pixel).
bayer[0::2, 0::2, 0::2] = 0  # Green pixels - set the blue and the red planes to zero (and keep the green)
bayer[0::2, 1::2, 0:2] = 0  # Red pixels - set the blue and the green planes to zero (and keep the red)
bayer[1::2, 0::2, 1:] = 0  # Blue pixels - set the red and the green planes to zero (and keep the blue)
bayer[1::2, 1::2, 0::2] = 0  # Green pixels - set the blue and the red planes to zero (and keep the green)

bayer = cv2.resize(bayer, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)
cv2.imwrite('bayer1.png', bayer)

print(bayer.shape)
