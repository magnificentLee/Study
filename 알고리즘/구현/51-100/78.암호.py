# 문자열을 최상단부터 오른쪽 -> 왼쪽 -> 아래 -> 오른쪽 순으로 읽는것에 주의
# 각 행을 주어진 문자열만큼 채워서 전체 길이 // 문자열 = 전체 행
k = int(input())
n = input()
l = len(n) // k
array = ["" for _ in range(l)]
tmp = ""
idx = 0
for i in range(l):
    if (i + 1) % 2 == 0:
        array[i] = n[idx + k - 1: idx - 1: -1]
    else:
        array[i] = n[idx: idx + k]
    idx += k  # 예제인 3 기준으로 진행하면서 상수 3으로 적는 바람에 오답처리됨
for i in range(k):
    for j in range(l):
        tmp += array[j][i]
print(tmp)