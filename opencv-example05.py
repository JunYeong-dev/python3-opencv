import cv2
import matplotlib.pyplot as plt

image = cv2.imread('cat.jpg')
# 모든 범위에서 B, G, R중 2에 해당하는 R을 0으로 바꿔줌
image[:, :, 2] = 0

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()