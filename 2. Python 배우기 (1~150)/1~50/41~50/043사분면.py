# 각 사분면과 축에 점이 몇 개 있는지
"""
input
5
0 0
0 1
1 1
3 -3
2 2
output
Q1: 2
Q2: 0
Q3: 0
Q4: 1
AXIS: 2
"""
n = int(input())
Q1 = Q2 = Q3 = Q4 = AXIS = 0
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0: # AXIS를 else에 만든게 틀린 원인 같음
        AXIS += 1
    elif x > 0:
        if y > 0:
            Q1 += 1
        else:
            Q4 += 1
    elif x < 0:
        if y > 0:
            Q2 += 1
        else:
            Q3 += 1
print("{}: {}".format("Q1", Q1))
print("{}: {}".format("Q2", Q2))
print("{}: {}".format("Q3", Q3))
print("{}: {}".format("Q4", Q4))
print("{}: {}".format("AXIS", AXIS))
