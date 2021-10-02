# 이항계수
"""
(n)   =  {  n! / (k!(n - k)!)  0 <= k <= n
(k)      {      0              k < 0
         {      0              k > n
"""
# 조건을 확인하면 0 <= k <= n 이다
# math 모듈을 사용하는 방법
""" 
from math import factorial as fac
n, k = map(int, input().split())
if k < 0 or k > n:
    print(0)
else:
    print(int(fac(n) / (fac(k) * fac(n - k))))
"""
n, k = map(int, input().split())
up = 1
down1 = 1
down2 = 1
for i in range(1, n + 1):
    up *= i
for i in range(1, k + 1):
    down1 *= i
for i in range(1, n - k + 1):
    down2 *= i
print(int(up / (down1 * down2)))