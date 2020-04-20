import cv2

image = cv2.imread('cat.jpg')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 Numpy 객체의 특정 픽셀을 선택
px = image[100, 100]

# B, G, R 순서로 출력
# (단, Gray Scale인 경우에는 B, G, R로 구분되지 않음)
print(px)

# R값만 출력
print(px[2])