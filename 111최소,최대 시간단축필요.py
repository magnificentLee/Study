# 마지막, 메모리, 시간 단축/ 428ms, 114B
import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
print(min(n_list), max(n_list))

""" 1차 432ms, 89B
n = int(input())
n_list = list(map(int, input().split()))
print(min(n_list), max(n_list))
"""

"""or
n_list = list(map(int, input().split()))
n_list = sorted(n_list)
print(n_list[0], n_list[n - 1])
"""
"""or
a = list(map(int, input().split()))
print(f"{min(a)} {max(a)}")
"""