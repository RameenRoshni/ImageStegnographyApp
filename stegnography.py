import cv2
import numpy as np

cover = cv2.imread("images/cover.png")
secret = cv2.imread("images/medimage.png")

secret = cv2.resize(secret, (cover.shape[1], cover.shape[0]))

encoded = (cover & 254) | (secret >> 7)
cv2.imwrite("encoded.png", encoded)

encoded = cv2.imread("encoded.png")

decoded = np.zeros_like(encoded)

for i in range(encoded.shape[0]):
    for j in range(encoded.shape[1]):
        for k in range(3):
            decoded[i,j,k] = (encoded[i,j,k] & 1) * 255

cv2.imwrite("decoded.png", decoded)
