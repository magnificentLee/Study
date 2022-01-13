# 참가자수, 예산, 호텔의수, 주의개수 = n, b, h, w
# 호텔의 정보1 : 1일당 숙박비용
# 호텔의 정보2 : i번째 주에 투숙 가능한 인원
# 즉, i번째 주의 투숙 가능한 인원이 참가자수보다 낮으면 다음 호텔로
# 가능하면 참가자수*숙박비용 = min값
# 반복문으로 다음 호텔도 돌면서 min값을 최신화해준게 정답일듯
# 호텔의 수 18, 주의 개수13 이므로 처음에 정렬X
# 풀이1
from sys import stdin
input = stdin.readline

n, b, h, w = map(int, input().split())
tmp, result = 0, []
for _ in range(h):
    p = int(input())
    array = sorted(map(int, input().split()))
    for i in array:
        if i >= n:
            tmp = p * n
            if tmp > b:
                break
            else:
                result.append(tmp)
if not result:
    print("stay home")
else:
    print(min(result))

""" 반례 최초정답 전까지 틀렸던것
3 1000 4 3
200
0 2 2
300
27 3 20
200
0 3 3
250
2 1 4
output = 250 (250 * 1)
정답 = 600 (200 * 3)
"""