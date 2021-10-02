# 내림차순 : 수가 차례로 내려가는것
x = int(input())

for i in range(1, x + 1):
    n = list(map(int, input().split()))
    t = n.pop(0)
    m = sorted(n)[::-1]
    old_gap = 0
    for j in range(t - 1):
        if m[j] - m[j + 1] > old_gap:
            old_gap = m[j] - m[j + 1]
    print("Class %d" % i)
    print("Max {}, Min {}, Largest gap {}".format(max(m), min(m), old_gap))
