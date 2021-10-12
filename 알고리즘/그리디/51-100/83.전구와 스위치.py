from sys import stdin
input = stdin.readline

n = int(input())
initial = list(map(int, input().rstrip("\n")))
result = list(map(int, input().rstrip("\n")))

def change(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num


def switch(ini, cnt):
    count = cnt
    if count == 1:
        ini[0] = change(ini[0])
        ini[1] = change(ini[1])
    for i in range(1, n):
        if ini[i - 1] != result[i - 1]:
            count += 1
            ini[i - 1] = change(ini[i - 1])
            ini[i] = change(ini[i])
            if i != n - 1:
                ini[i + 1] = change(ini[i + 1])
    if ini == result:
        return count
    else:
        return -1


result1 = switch(initial[:], 0)
result2 = switch(initial[:], 1)
if result1 >= 0 and result2 >= 0:
    print(min(result1, result2))
elif result1 >= 0 and result2 < 0:
    print(result1)
elif result1 < 0 and result2 >= 0:
    print(result2)
else:
    print(-1)
