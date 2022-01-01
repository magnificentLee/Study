# 일반적인 풀이와 이진탐색을 이용한 풀이 두 가지가 존재함
# 이진탐색으로 어떻게 풀어야할지 감이 안 왔음
# 거리가 홀 수일 때 빈공간 1이 남는다는 것에 주의
n = int(input())
m = int(input())
array = list(map(int, input().split()))
light, height = array[0], array[0]
for i in range(1, len(array)):
    tmp = array[i] - light

    if tmp % 2 == 0:  # 양수면
        tmp //= 2
    else:  # 음수면 빈공간이 1만큼 남기 때문에 +1
        tmp = (tmp // 2) + 1

    height = max(height, tmp)
    light = array[i]
result = max(height, abs(n - array[-1]))
print(result)