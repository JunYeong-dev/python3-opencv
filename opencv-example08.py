import cv2
import matplotlib.pyplot as plt

# 이미지 회전
# - 회전 변환을 위한 기본적인 행렬은 다음과 같음
# | cosθ -sinθ |
# | sinθ  cosθ |
# - 이 때 무게 중심을 적용할 수 있는 회전 변환 식은 다음과 같이 정의할 수 있음
# α = scale * cosθ
# β = scale * sinθ 일 때
# |  α β (1 - α) * center.x - β * center.y |
# | -β α β * center.x + (1 - α) * center.y |

# cv2.getRotationMatrix2D(center, angle, scale) : 이미지 회전을 위한 변환 행렬을 생성
# center : 회전 중심
# angle : 회전 각도
# scale : Scale Factor

image = cv2.imread('cat.jpg')

# 행과 열 정보만 저장
height, width = image.shape[:2]

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()


