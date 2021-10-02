# 모든 밧줄을 이용했을 경우 버틸 수 있는 최대 중량을 구한 경우
# 문제를 잘못 이해한경우임
n = int(input())

ropes = [int(input()) for _ in range(n)]
if len(ropes) == 1:
    print(ropes[0])
else:
    print(min(ropes) * n)
print(sorted(ropes, reverse=True))