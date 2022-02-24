# 백준 20921 그렇고 그런 사이
# 입력 값만큼의 요소의 갯수를 가지는 리스트를 구하되
# 다음과 같은 특징을 가지게 하라
# 인덱스상 좌측의 값이 우측의 값보다 큰 경우 카운트, 최종적으로 입력값이 되게끔
# 예를 들어
# 5 7
# 5 1 4 3 2
# 해석하자면 5 1, 5 4, 5 3, 5 2, 4 3, 4 2, 3 2 = 총 7개
n, k = list(map(int, input().split()))
array = [i + 1 for i in range(n)]

result = []
for i in range(n - 1, -1, -1):
    target = min(k, i)  # i = maxV
    k -= target
    result.append(array.pop(target))
print(*result)
