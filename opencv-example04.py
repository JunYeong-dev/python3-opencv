import cv2
import matplotlib.pyplot as plt

image = cv2.imread('cat.jpg')

# Numpy Slicing : ROI(Region of Interest; 관심영역) 처리 가능
roi = image[150:300, 50:200]

# ROI 단위로 이미지 복사하기
image[0:150, 0:150] = roi

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()