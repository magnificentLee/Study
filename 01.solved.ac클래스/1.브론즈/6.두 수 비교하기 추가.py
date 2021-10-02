# 수의 범위가 넓지 않아서 시간 차이가 없음
"""
from sys import stdin
a, b = map(int, stdin.readline().split())
print(">" if a > b else "<" if a < b else "==")
"""
a, b = map(int, input().split())
print(">" if a > b else "<" if a < b else "==")