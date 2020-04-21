import cv2
# 다양한 데이터를 도식화 하는데 사용하는 라이브러리
import matplotlib.pyplot as plt
import time

image = cv2.imread('cat.jpg')

# 하나의 픽셀마다 전부 접근 하여 바꿔줘야 하기 때문에 시간이 상대적으로 오래 걸림
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))
# matplotlib에서는 RGB 순서이기 때문에 BGR -> RGB로 변환
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# 슬라이싱 연산을 이용하면 훨씬 빠른 속도로 변환이 가능
start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()