import cv2
import numpy as np

# Filtering 필터링
# 이미지에 커널을 적용하여 이미지를 흐리게(Blurring = Smootihing) 처리할 수 있음
# 이미지를 흐리게 만들면 노이즈 및 손상을 줄일 수 있음

# 컨볼루션 계산
# 특정한 이미지에 커널(Kernel)을 적용해 컨볼루션 계산하여 필터링을 수행할 수 있음

# (3, 3)의 값 2에 적용하려는 상황
# 원본 이미지    커널
# 5 4 3 2 5
# 4 6 5 4 3     1 2 1
# 7 5 2 5 9     2 5 2
# 8 5 6 1 3     1 2 1
# 5 7 7 8 6

# 동일한 위치에서 각각의 값들을 곱해주는 것
# 결과
# 6*1 5*2 4*1        6  10 4
# 5*2 2*5 5*2   =>   10 10 10
# 5*1 6*2 1*1        5  12 1

# 커널 값의 총합 => 17
# 결과 값의 총합 => 68
# 결과 값의 총합을 커널 값의 총합으로 나눈 값을 대상 픽셀의 값으로 쓰겠다는 것
# 68 / 17 = 4
# 즉, (3, 3)의 값 2를 4로 변환

# 커널의 종류 예
# Basic Kernel
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1   *   1/25
# 1 1 1 1 1
# 1 1 1 1 1

# Gaussian Kernel
# 1 4  7  4  1
# 4 16 26 16 4
# 7 26 41 26 7   *   1/273
# 4 16 26 16 4
# 1 4  17 4  1

# Kernel을 직접 설정하는 방법
image = cv2.imread('cat.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

size = 4
kernel = np.ones((size, size), np.float32) / (size ** 2)
print(kernel)
# kernel
# 1/16 1/16 1/16 1/16
# 1/16 1/16 1/16 1/16
# 1/16 1/16 1/16 1/16
# 1/16 1/16 1/16 1/16
dst = cv2.filter2D(image, -1, kernel)
cv2.imshow('Image', dst)
cv2.waitKey(0)

# Basic Blur
image = cv2.imread('cat.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

dst = cv2.blur(image, (4, 4))
cv2.imshow('Image', dst)
cv2.waitKey(0)

# Gaussian Blur
image = cv2.imread('cat.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

# kernel_size : 홀수
dst = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Image', dst)
cv2.waitKey(0)





