""" 0 1 1 2 3 5 8 13 21 34 ....
ans1 = 0 + 1 = ans0 + ans
ans2 = 1 + 1 = ans1 + ans0
ans3 = 2 + 1 = ans2 + ans1
ans4 = 3 + 2 = ans3 + ans2
"""
n = int(input())
a = 0
b = 1
c = 0
for i in range(n):
    c = a
    a = b  # result
    b = c + b
print(a)