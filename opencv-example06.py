import cv2
import matplotlib.pyplot as plt

# cv2.resize(image, dsize, fx, fy, interpolation) : 이미지의 크기를 조절
# dsize : Manual Size
# fx : 가로 비율
# fy : 세로 비율
# interpolation(보간법) : 사이즈가 변할 때 픽셀 사이의 값을 조절하는 방법
# INTER_CUBIC : 사이즈를 크게 할 때 주로 사용
# INTER_AREA : 사이즈를 작게 할 때 주로 사용

image = cv2.imread('cat.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
plt.imshow(cv2.cvtColor(expand, cv2.COLOR_BGR2RGB))
plt.show()

shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB))
plt.show()