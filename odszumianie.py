import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

image = Image.open('leopard.jpg')
org = Image.open('Leopard-1.jpg')
image = np.array(image)


def denoise_image(image):
    # Tworzymy obraz wynikowy o takiej samej wielkości jak obraz wejściowy
    denoised_image = np.empty_like(image)

    # Przechodzimy przez każdy piksel obrazu
    for y in range(1, image.shape[0] - 1):
        for x in range(1, image.shape[1] - 1):
            # Wyznaczamy najbliższych sąsiadów danego piksela
            neighbors = image[y - 1:y + 2, x - 1:x + 2]
            # Zastępujemy wartość danego piksela wartością mediana z jego sąsiadów dla każdego z kanałów kolorów
            denoised_image[y, x] = np.median(neighbors, axis=(0, 1))

    return denoised_image
denoised_image = denoise_image(image)
odej = ((image - denoised_image)**2)

dift = (org - denoised_image)**2
cv2.imwrite('odej.png', dift)

plt.imshow(denoised_image)
plt.show()
