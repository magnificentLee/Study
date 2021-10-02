t = int(input())

for _ in range(t):
    n, m = list(map(str, input().split()))
    count_zero, count_one = 0, 0
    for i in range(len(n)):
        if n[i] == m[i]:
            continue
        else:
            if n[i] == "1":
                count_one += 1
            else:
                count_zero += 1
    print(max(count_zero, count_one))
