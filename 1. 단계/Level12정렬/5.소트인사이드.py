import sys

n = sorted(list(sys.stdin.readline()), reverse=True)
[print(i, end="") for i in n]