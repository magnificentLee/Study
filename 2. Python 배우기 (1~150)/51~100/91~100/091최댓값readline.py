import sys

data = []

for i in range(9):
    n = int(sys.stdin.readline())
    data.append(n)
print(max(data), data.index(max(data)) + 1)  # 0을 고려해야하기 때문에 +
"""
n 을 나눠준 경우 : 60ms 138B
나눠주지 않은 경우: 64ms 128B
input 을 사용한경우:72ms 94B
"""