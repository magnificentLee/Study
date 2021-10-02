# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
# 이하 입력/출력
"""
Input
5
5
2
3
4
1
Output
1
2
3
4
5
"""
import sys

t = int(input())
num_list = []
for i in range(t):
    n = int(sys.stdin.readline())
    num_list.append(n)
num_list = sorted(num_list)
for i in num_list:
    print(i)
