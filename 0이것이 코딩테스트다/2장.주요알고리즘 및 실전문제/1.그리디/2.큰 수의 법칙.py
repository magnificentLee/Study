# 내 풀이
n, m, k = map(int, input().split())
num = sorted(map(int, input().split()), reverse=True)

top = num[0]
top_2nd = num[1]

result = 0
for i in range(m):
    if (i + 1) % k == 0:
        result += top_2nd
    else:
        result += top
print(result)
