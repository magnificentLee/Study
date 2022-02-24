# 해석하자면 총 n명의 인원 중에서 k개의 커플을 생기게 하라는 건데
# 좌측이 우측보다 값이 크다면(같은 경우는 없음) 커플, 작다면 X
# 좌측에만 있으면 됨, 값이 떨어져 있어도 괜찮음
# 예제
# 5 7
# 5 1 4 3 2
# 해석하자면 5 1, 5 4, 5 3, 5 2, 4 3, 4 2, 3 2 = 총 7개
# 단, 리스트를 주는게 아닌 리스트를 만드는 것이기 때문에 어떻게 해야 될지 모르겠음
# 아래는 반대로 리스트를 이용해 갯수를 구하는 것, 아마 브론즈 난이도 수준일 것임
"""
n, k = map(int, input().split())
array = [5, 1, 4, 3, 2]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if array[i] > array[j]:
            count += 1
print(count)
"""
n, k = list(map(int, input().split()))
array = [i + 1 for i in range(n)]

result = []
for i in range(n - 1, -1, -1):
    target = min(k, i)  # i = maxV
    k -= target
    result.append(array.pop(target))
print(*result)
