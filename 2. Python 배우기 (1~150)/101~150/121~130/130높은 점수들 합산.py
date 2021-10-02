import sys

a = []
b = []
for i in range(10):
    a.append(int(sys.stdin.readline()))
a = sorted(a)[::-1]
a_sum = sum(a[0:3])
for i in range(10):
    b.append(int(sys.stdin.readline()))
b = sorted(b)[::-1]
b_sum = sum(b[0:3])
print(a_sum, b_sum)