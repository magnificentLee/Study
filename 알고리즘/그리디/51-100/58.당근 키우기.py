# 직접 그려보면서 규칙을 찾아보면
# x + y + min(x // 10, y // 10) 이 나온다
from sys import stdin

x, y = map(int, stdin.readline().split())
result = x + y + min(x // 10, y // 10)
print(result)
# math 라이브러리를 이용하는 방법
"""
import math
x, y = map(int, input().split()) #온기, 수분
print(math.trunc(x + y + (min(x, y) / 10))) #trunc == 버림
"""