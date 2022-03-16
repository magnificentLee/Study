# 백준 5883 아이폰9S
# pop을 사용하면 기존의 리스트에도 영향이감
# tmp = array로 설정하고 tmp.pop을 사용하면 기존의 array에도 영향이 간다는 말임
# 당연하지만 3중 for문 떄문에 시간초과
from sys import stdin
input = stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
val = -1  # 요소는 0~ 1,000,000 이기 때문에 영향이 없는 -1로 설정
count = 0
result = 0
for i in set(array):
    for j in array:
        if i != j:
            if val == j:
                count += 1
            else:
                val = j
                result = max(result, count)
                count = 1
result = max(result, count)  # 마지막에 count가 최다가 되는 경우 때문
print(result)