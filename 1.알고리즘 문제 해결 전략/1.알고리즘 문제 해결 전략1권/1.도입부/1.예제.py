# 록 페스티벌 난이도 하
# 최솟값을 구하는 문제
"""
INPUT
2
6 3
1 2 3 1 2 3
6 2
1 2 3 1 2 3
OUTPUT
1.7500000000
1.5000000000
"""

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())  # 리스트길이, 팀 수
    array = list(map(int, input().split()))
    result = max(array)
    for i in range(n - k):
        j = k
        while True:
            if (i + j) >= n:
                break
            tmp = array[i:i + j]
            up = sum(tmp)
            down = len(tmp)
            result = min(result, up / down)
            j += 1
    print("%.10f" % result)