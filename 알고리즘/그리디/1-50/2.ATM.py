n = int(input())
val = sorted(map(int, input().split()))
time = 0
result = 0
for i in val:
    time += i
    result += time
print(result)