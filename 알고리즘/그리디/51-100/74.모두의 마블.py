# 빈 리스트에 추가하는 방식은 시간초과가 발생할 것임
# for 문에 pop 방식을 쓰면 에러가 발생할 것
# while문? for 문 비슷하게 만드는 방법이 있지만 쉬운 방법을 생각하면
# 종이에 적어서 공통점을 찾아보면 내림차순으로 정렬했을 때 인덱스0 과 나머지 값을 누적해서 더하는 방식임
from sys import stdin
input = stdin.readline

n = int(input())
card = sorted(map(int, input().split()), reverse=True)
result = 0
for i in range(n):
    if i <= 1:
        result += card[i]
    else:
        result += card[0] + card[i]
print(result)