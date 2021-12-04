# 최대한 줄였던 방식, 시간은 변화 없음
# 아마 상위권들의 제출시간이 1~2년전인것으로 보아 옛날 서버 기준이라 그런것 같음
l = int(input())
r = int(input())
x, y, res = 1, 0, 0
while True:
    x *= 2
    y = int(l * (r / 100))
    if y <= 5:
        break
    l = y
    res += l * x
print(res)

# 처음 풀었던 방식, 맞았지만 묘하게 느림
"""
l = int(input())
r = int(input())
x, y = 1, 0
branch = [(x, y)]
while True:
    x *= 2
    y = int(l * (r / 100))
    if y <= 5:
        break
    else:
        branch.append((x, y))
        l = y
result = 0
for i, j in branch:
    result += i * j
print(result)
"""

