t = int(input())
n = sorted(map(int, input().split()))
# 3 1 4 3 2 -> 1 2 3 3 4
time = 0
result = 0
for i in n:
    time += i
    result += time
print(result)
# 1 / 1 + 2 / 1 + 2 + 3 / 1 + 2 + 3 + 3 / 1 + 2 + 3 + 3 + 4
# 1 + 3 + 6 + 9 + 13 = 32