# 백준 2485 가로수
# 최대공약수 문제, 문제의 핵심이 최대공약수라는 점과 이를 구현 혹은 math 함수를 이용하는 것에 중점
# 2중 for문을 이용했다가 틀렸었음
# Input
# 4
# 1
# 3
# 7
# 13
# Output
# 3(갯수)
# 1~3~7~13
# 2 4 6

# if 1 3 5 7 13
# 2 2 2 6

# if 1 3 5 7 9 11 13
# 2 2 2 2 2 2
# : 5 9 11 = 3

# 2 4 6 의 최대공약수 = 2,  2 4 6을 2로 나누면 = 1, 2, 3 / 1 2 3 을 각각 1을 뺀 뒤 더하면 0+1+2 = 3
# 최대공약수를 구하는 함수
from sys import stdin
input = stdin.readline

def gcd(a, b):
    while b != 0:
        res = a % b
        a = b
        b = res
    gcd = a
    return gcd


n = int(input())
pos = [int(input()) for _ in range(n)]
length = []  # 각 지점 사이의 값(최대공약수를 구하기 위함)
past_pos = pos[0]
for i in range(1, n):
    tree = pos[i]
    tmp = tree - past_pos
    length.append(tmp)
    past_pos = tree
# 최대공약수를 저장하기 위한 리스트와 리스트를 채우는 과정, 최대공약수는 리스트의 최솟값임(계산해보면 알음)
gcd_val = max(length)
for i in range(1, len(length)):
    gcd_tmp = gcd(length[0], length[i])
    gcd_val = min(gcd_tmp, gcd_val)
result = 0
for i in range(len(length)):
    result += (length[i] // gcd_val) - 1
print(result)
