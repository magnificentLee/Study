import random
array = [random.randrange(0, 105) for _ in range(100)]
# 의도적으로 입력값의 최대를 array의 길이보다 크게 설정해놓음 = 인덱스 초과가 나오게끔끔
count = [0] * (max(array) + 1)  # 0을 포함하기 때문에 +1

for i in range(100):
    count[array[i]] += 1
for i in range(100):
    for j in range(count[i]):
        print(i, end=" ")
