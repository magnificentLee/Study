# 주차장은 모든 정수좌표에 있으므로 i = 0, 주차장겸 상점, 끝까지 갔다가 돌아오는걸 고려(거리*2)
# 68ms, 150B
import sys

for i in range(int(input())):
    n = int(input())
    m = sorted(map(int, sys.stdin.readline().split()))
    print((max(m) - min(m)) * 2)
""" 76ms, 125B 
for i in range(int(input())):
    n = int(input())
    m = sorted(map(int, input().split()))
    print((max(m) - min(m)) * 2)
"""