""" 1차 시도
n = int(input())
for i in range(1, 10):
    print(n, "*", i, "=", n * i)
"""
# 2차 시도 format을 이용한 방법
n = int(input())
for i in range(1, 10):
    print("{} * {} = {}".format(n, i, n * i))