n = int(input())
a = 0
b = 1
c = 0
for i in range(n):
    c = a
    a = b # result
    b = c + b
print(a)
