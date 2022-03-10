# 백준 10815 숫자 카드
# 수의 범위가 매우 넓고 값도 많은데다 섞여있음
# 최악의 경우를 생각해야함, 최악의 경우에서 가장 빠른 정렬들은 힙, 병합, 팀이 있으며 모두 최악의 경우 시간복잡도는 동일함
# 파이썬에서 sort 함수는 팀 정렬을 이용하기 때문에 sort로 미리 정렬한 다음 이진탐색을 이용해 출력하면 될 것 같음
# 1차 : 111356kb, 3572ms 로 통과
"""
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
    print(binary(i, 0, n - 1), end=" ")
"""
# 위 코드에서 빠른 입력을 이용한 경우 : 112652kb, 3508ms = 유의미한 차이X
"""
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
    print(binary(i, 0, n - 1), end=" ")
"""
# 의문점
# 시간복잡도를 줄이기 위해 다른 사람들의 코드도 확인했는데
# 미리 sorted를 하지 않고 선언 이후 sort 처리를 하던데 이유가 있을까?
# 2차 (빠른 입력 사용) : 112668kb, 3512ms : 유의미한 차이는 없음
# 처음부터 sorted 하는게 조금 더 빠르기 때문에 그렇게 하는게 좋을 것 같음
"""
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
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
for i in b:
    print(binary(i, 0, n - 1), end=" ")
"""
# 다만 이전의 수 찾기 같이 집합을 이용해 빠르게 푸는 방법이 있다는 것을 알기 때문에
# 이를 이용해보면 (빠른 입출력을 이용한 경우): 123652kb, 516ms
"""
from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        stdout.write("1 ")
    else:
        stdout.write("0 ")
"""
# 다른 사람 코드를 이용한 빠른 코드
# 가장 빠른 방법 : 122620kb 432ms
from sys import stdin
input = stdin.readline

def solution():
    input()
    a = set(input().split())
    input()
    b = input().split()
    res = ""
    for i in b:
        if i in a:
            res += "1 "
        else:
            res += "0 "
    print(res)
solution()
