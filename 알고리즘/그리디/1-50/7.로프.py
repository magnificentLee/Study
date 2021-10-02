# 로프가 각각 100, 99, 10 을 버틴다고 할 때
# 100 하나면 100/ 100, 99 두 개면 198/ 100, 99, 10 세 개면 30밖에 못 버팀
# 따라서 임의로 몇 개의 로프를 선발해서 최댓값을 구하는 문제임 (모두 사용하라는 말이 아님)
# 각각의 로프는 w/k 만큼 버틸 수 있음, 따라서 최대는 로프하중 * k (100+99)*2 = 398
# 100 80 60 40 20 일 때 / 100*1, 80*2, 60*3, 40*4, 20*5 / 최대는 180
from sys import stdin
n = int(stdin.readline())
rope = sorted([int(stdin.readline()) for _ in range(n)], reverse=True)
result = 0
for i in range(n):
    if result < rope[i] * (i + 1):  # result가 최대하중보다 낮다면 result = 최대하중으로 치환
        result = rope[i] * (i + 1)
print(result)