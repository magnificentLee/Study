import math
n = int(input())
m = int(input())
result = []
for i in range(int(math.sqrt(n)), int(math.sqrt(m)) + 1):
    if i ** 2 >= n:
        result.append(i ** 2)
if not result:
    print(-1)
else:
    print(sum(result), result[0], sep="\n")