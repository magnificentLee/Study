# 백준 1920 수 찾기
# 기본 풀이 : 정렬과 이진탐색을 이용
# 선형탐색을 이용할 경우 무조건 시간초과 발생
from sys import stdin
input = stdin.readline

def binary(target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if a[mid] == target:
        return 1
    elif a[mid] > target:
        return binary(target, start, mid - 1)
    else:
        return binary(target, mid + 1, end)


n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in b:
    print(binary(i, 0, n - 1))

# 집합과 빠른 입출력을 이용하는 방법, 6배정도 빠름
"""
from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        stdout.write("1\n")
    else:
        stdout.write("0\n")
"""
