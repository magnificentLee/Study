"""
def get_stars(num):
    matrix = []
    for i in range(3 * len(num)):
        if i // len(num) == 1:  # 가운데 빈 공간용
            matrix.append(num[i % len(num)] + " " * len(num) + num[i % len(num)])
        else:
            matrix.append(num[i % len(num)] * 3)
    return matrix
n = int(input())
star = ["***", "* *", "***"]
e = 0
while n != 3:
    n = int(n / 3)
    e += 1
for i in range(e):
    star = get_stars(star)
for i in star:
    print(i)
"""
"""
def star(i):
    global arr
    idx = [i for i in range(n) if (i // 3 ** cnt_) % 3 == 1]
    for i in idx:
        for j in idx:
            arr[i][j] = " "

n = int(input())
v = n
cnt = 0
while v != 1:
    v /= 3
    cnt += 1

arr = [["*"] * n for _ in range(n)]
for cnt_ in range(cnt):
    star(cnt_)

print("\n".join(["".join([str(i) for i in row]) for row in arr]))
"""