"""
input
2      : 총 테스트 케이스 갯수
10000  : 1번 테스트, 자동차 가격
2      : 1번 테스트, 옵션 종류
1 2000 : 1번 테스트, 옵션 갯수, 가격
3 400  : 1번 테스트, 옵셧 갯수, 가격
50000  : 2번 테스트, 자동차 가격
0      : 2번 테스트, 옵션 갯수
output
13200
50000
"""
t = int(input())

for i in range(t):
    s = int(input())  # 자동차 가격
    n = int(input())  # 옵션의 갯수
    total = 0

    for j in range(n):
        q, p = map(int, input().split())
        total += q * p

    print(total + s)
