# 빠른 입출력이 있고 없고의 차이 : 시간이 약 3배 차이남
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    array = [int(input()) for _ in range(n)]
    half = sum(array) // 2
    m = max(array)
    idx = array.index(m) + 1
    m_count = array.count(m)
    if m_count > 1:
        print("no winner")
    else:
        if m <= half:
            print("minority winner %i" % idx)
        else:
            print("majority winner %i" % idx)