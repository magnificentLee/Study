# 백준 4539 반올림
# 반올림 모듈을 이용하지 않고 직접 구현하는게 목적
# 끝에서 큰수로 돌면서 반올림 가능한지 확인, 5이상이면 그 앞 자리에 +1, 해당 자리는 0, 아니라면 해당 자리는 0
from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
    n = list(input().rstrip())
    l = len(n)
    for i in range(l - 1, 0, -1):
        if int(n[i]) >= 5:
            n[i - 1] = str(int(n[i - 1]) + 1)
        n[i] = "0"
    print(*n, sep="")