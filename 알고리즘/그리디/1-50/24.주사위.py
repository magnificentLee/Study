# n^3 개의 주사위로 n * n * n 의 정육면체를 만들어
# 총 6면중 밑면을 제외한 5면에서 보이는 주사위 수 합의 최솟값을 구하는 문제
# 1면이 보이는 개수 : (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2) 개
# 2면이 보이는 개수 : 4 * (n - 2) + 4 * (n - 1) 개
# 3면이 보이는 개수 : 정육면체의 각 꼭짓점 : 4개
from sys import stdin

n = int(stdin.readline())
dice = list(map(int, stdin.readline().split()))

if n == 1:
    print(sum(dice) - max(dice))
else:
    sumlist = [min(dice[0], dice[5]),
               min(dice[1], dice[4]),
               min(dice[2], dice[3])]
    sumlist.sort()
    n1 = (n - 2) * (n - 2) + (n - 1) * (n - 2) * 4
    n2 = (n - 2) * 4 + (n - 1) * 4
    n3 = 4
    result = n1 * sumlist[0] + n2 * sum(sumlist[:2]) + n3 * sum(sumlist)
    print(result)