a = input().split()
n = int(a[0])
s = a[1]
array = [input().split() for _ in range(n)]
count = 0
for i in range(n - 1, -1, -1):
    if array[i][0] == s:
        idx = i
        result = array[i][1]
for i in range(idx - 1, -1, -1):
    if array[i][1] == result:
        count += 1
print(count)