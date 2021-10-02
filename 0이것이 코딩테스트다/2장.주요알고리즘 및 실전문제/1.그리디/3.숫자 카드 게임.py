# n : 행(세로 길이), m : 열
import sys

n, m = map(int, input().split())
l_list = []
for i in range(n):
    num = map(int, sys.stdin.readline().split())
    l_list.append(min(num))
print(max(l_list))
