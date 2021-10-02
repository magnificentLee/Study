from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 선택 정렬 프로글매 성능 측정
start_time = time.time()

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

end_time = time.time()
print("선택 정렬 성능 측정:", end_time - start_time)  # 수행 시간 측정
# 결과 : 약 7.45 초  / 책 : 35.84초
