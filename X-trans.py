import numpy as np
import cv2

im = cv2.imread('strus.bmp')
im = cv2.resize(im, None, fx=1 , fy=1 , interpolation=cv2.INTER_NEAREST)
(height, width) = im.shape[:2]
(B, G, R) = cv2.split(im)

bayer = np.empty((height, width), np.uint8)

# striped slicing for this pattern:
#   G B R G R B
#   R G G B G G
#   B G G R G G
#   G R B G B R
#   B G G R G G
#   R G G B G G

bayer[0::6, 0::6] = G[0::6, 0::6]
bayer[0::6, 1::6] = B[0::6, 1::6]
bayer[0::6, 2::6] = R[0::6, 2::6]
bayer[0::6, 3::6] = G[0::6, 3::6]
bayer[0::6, 4::6] = R[0::6, 4::6]
bayer[0::6, 5::6] = B[0::6, 5::6]
bayer[1::6, 0::6] = R[1::6, 0::6]
bayer[1::6, 1::6] = G[1::6, 1::6]
bayer[1::6, 2::6] = G[1::6, 2::6]
bayer[1::6, 3::6] = B[1::6, 3::6]
bayer[1::6, 4::6] = G[1::6, 4::6]
bayer[1::6, 5::6] = G[1::6, 5::6]
bayer[2::6, 0::6] = B[2::6, 0::6]
bayer[2::6, 1::6] = G[2::6, 1::6]
bayer[2::6, 2::6] = G[2::6, 2::6]
bayer[2::6, 3::6] = R[2::6, 3::6]
bayer[2::6, 4::6] = G[2::6, 4::6]
bayer[2::6, 5::6] = G[2::6, 5::6]
bayer[3::6, 0::6] = G[3::6, 0::6]
bayer[3::6, 1::6] = R[3::6, 1::6]
bayer[3::6, 2::6] = B[3::6, 2::6]
bayer[3::6, 3::6] = G[3::6, 3::6]
bayer[3::6, 4::6] = B[3::6, 4::6]
bayer[3::6, 5::6] = R[3::6, 5::6]
bayer[4::6, 0::6] = B[4::6, 0::6]
bayer[4::6, 1::6] = G[4::6, 1::6]
bayer[4::6, 2::6] = G[4::6, 2::6]
bayer[4::6, 3::6] = R[4::6, 3::6]
bayer[4::6, 4::6] = G[4::6, 4::6]
bayer[4::6, 5::6] = G[4::6, 5::6]
bayer[5::6, 0::6] = R[5::6, 0::6]
bayer[5::6, 1::6] = G[5::6, 1::6]
bayer[5::6, 2::6] = G[5::6, 2::6]
bayer[5::6, 3::6] = B[5::6, 3::6]
bayer[5::6, 4::6] = G[5::6, 4::6]
bayer[5::6, 5::6] = G[5::6, 5::6]
# bayer = cv2.resize(bayer, None, fx=3, fy=3, interpolation=cv2.INTER_NEAREST)

bayer = cv2.cvtColor(bayer, cv2.COLOR_GRAY2BGR)  # Convert from Grayscale to BGR (r=g=b for each pixel).

bayer[0::6, 0::6, 0::2] = 0
bayer[0::6, 1::6, 1:] = 0
bayer[0::6, 2::6, 0:2] = 0
bayer[0::6, 3::6, 0::2] = 0
bayer[0::6, 4::6, 0:2] = 0
bayer[0::6, 5::6, 1:] = 0
bayer[1::6, 0::6, 0:2] = 0
bayer[1::6, 1::6, 0::2] = 0
bayer[1::6, 2::6, 0::2] = 0
bayer[1::6, 3::6, 1:] = 0
bayer[1::6, 4::6, 0::2] = 0
bayer[1::6, 5::6, 0::2] = 0
bayer[2::6, 0::6, 1:] = 0
bayer[2::6, 1::6, 0::2] = 0
bayer[2::6, 2::6, 0::2] = 0
bayer[2::6, 3::6, 0:2] = 0
bayer[2::6, 4::6, 0::2] = 0
bayer[2::6, 5::6, 0::2] = 0
bayer[3::6, 0::6, 0::2] = 0
bayer[3::6, 1::6, 0:2] = 0
bayer[3::6, 2::6, 1:] = 0
bayer[3::6, 3::6, 0::2] = 0
bayer[3::6, 4::6, 1:] = 0
bayer[3::6, 5::6, 0:2] = 0
bayer[4::6, 0::6, 1:] = 0
bayer[4::6, 1::6, 0::2] = 0
bayer[4::6, 2::6, 0::2] = 0
bayer[4::6, 3::6, 0:2] = 0
bayer[4::6, 4::6, 0::2] = 0
bayer[4::6, 5::6, 0::2] = 0
bayer[5::6, 0::6, 0:2] = 0
bayer[5::6, 1::6, 0::2] = 0
bayer[5::6, 2::6, 0::2] = 0
bayer[5::6, 3::6, 1:] = 0
bayer[5::6, 4::6, 0::2] = 0
bayer[5::6, 5::6, 0::2] = 0

bayer = cv2.resize(bayer, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)

cv2.imwrite('bayer.png', bayer)


