import cv2
import matplotlib.pyplot as plt

# Contour의 사각형 외각 찾기
# cv2.boundingRect(contour) : Contour를 포함하는 사각형을 그림
# 사각형의 X, Y 좌표와 너비, 높이를 반환

image = cv2.imread('digit_image.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR))
plt.show()

# findContours는 기본적으로 흰색을 추출하기 때문에 위쪽 작업으로 (흰색 배경, 검은색 글자) -> (검은색 배경, 힌색 글자)로 반전 시켜줌
contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

contour = contours[0]
x, y, w, h = cv2.boundingRect(contour)
image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()