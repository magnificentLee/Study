"""
Input
10
40
30
60
30
Output
34
30
"""
import sys

n_list = []

for i in range(5):
    n = int(sys.stdin.readline())
    n_list.append(n)
n_list = sorted(n_list)
avg = sum(n_list) // 5
avg_n = n_list[2]
print(avg, avg_n, sep="\n")