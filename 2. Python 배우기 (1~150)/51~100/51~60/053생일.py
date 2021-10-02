# 첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.
""" 람다를 사용한 방법
n = int(input())
age = {}
for i in range(n):
    data = input().split()
    age[data[0]] = [int(data[3]), int(data[2]), int(data[1])]
s = sorted(age.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))
print(s[0][0])
print(s[-1][0])
"""
import sys
input = sys.stdin.readline   # 해당 구문이 없으면 백준사이트에서 컴파일 에러가 발생함

n = int(input())
lst = []
for i in range(n):
    name, d, m, y = input().rstrip().split()
    if len(m) == 1:
        m = "0" + m
    if len(d) == 1:
        d = "0" + d
    lst.append((name, y + m + d))

lst.sort(key=lambda x: int(x[1]))
print(lst[-1][0])  # 역순으로 시작해서 가장 첫번째(최댓값)의 이름
print(lst[0][0])  # 가장 첫번째(최솟값)의 이름
