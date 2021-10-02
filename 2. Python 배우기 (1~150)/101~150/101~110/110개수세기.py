""" 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
Input
11
1 4 1 2 4 2 4 2 3 4 4
2
Output
3
"""
n = int(input())
count = 0
n_list = list(map(int, input().split()))
m = int(input())
for i in n_list:
    if i == m:
        count += 1
print(count)
