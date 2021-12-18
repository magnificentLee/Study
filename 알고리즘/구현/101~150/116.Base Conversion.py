a, b = map(int, input().split())
m = int(input())
array = list(map(int, input().split()))
array.reverse()
tmp = 0
result = []
for i in range(m):
    tmp += array[i] * (a ** i)
while tmp != 0:
    result.append(tmp % b)
    tmp //= b
print(*reversed(result))