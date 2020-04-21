import cv2
import numpy as np
import matplotlib.pyplot as plt

# cv2.warpAffine(image, M, dsize) : 이미지의 위치를 변경
# M : 변환행렬
# dsize : Manual Size
# 변환 행렬과 변환
# - 변환 행렬의 형태
# | M₁₁ M₁₂ M₁₃ |
# | M₂₁ M₂₂ M₂₃ |
# - 이미지의 모든 좌표 (a, b)는 다음의 좌표로 이동
# (M₁₁ * a + M₁₂ * b + M₁₃, M₂₁ * a + M₂₂ * b + M₂₃)
# 이미지 위치 변경
# - 단순히 이미지의 위치를 변경할 떄 변환 행렬은 다음과 같다
# | 1 0 tx |
# | 0 1 ty |
# - 이미지의 모든 좌표(a, b)는 다음의 좌표로 이동
# (a + tx, b + ty)

image = cv2.imread('cat.jpg')

# 행과 열 정보만 저장
height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()