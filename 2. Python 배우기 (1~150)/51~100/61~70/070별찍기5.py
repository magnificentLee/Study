"""
    *
   ***
  *****
 *******
*********
"""
# 1 3 5 7 9 ...
n = int(input())
a = 1
for i in range(1, n + 1):
    a = i * 2 - 1
    n -= 1
    print(" " * n + "*" * a)