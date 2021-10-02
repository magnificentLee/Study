from random import randint
import time

array = []
for _ in range(1, 10000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)
# 결과 : 0.0009999 초 / 책 : 약 0.001339 초
