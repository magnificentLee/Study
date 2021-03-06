# n은 절댓값이 1,000,000을 넘지 않는 정수
# 출력시 절댓값을 1,000,000,000으로 나눈 나머지를 출력
# 일반적인 반복문을 이용한 재귀적인 풀이는 절대로 풀 수 없음
# 다행히 시간제한으 2초로 dp 배열을 이용한 풀이가 가능 할 수도 있지만 시간을 더 줄일 수 있는
# 치환을 이용한 방법을 사용할 예정
# 문제 설명에 있는 내용을 바탕으로 패턴을 구해본 결과
# n = 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6
#     8 5 3 2 1 1 0  1 -1  2 -3  5 -8
# 즉, n이 음수일 때 홀수라면 양수, 짝수라면 음수가 나옴
n = int(input())
a, b = 0, 1
m = abs(n)
for i in range(m):
    a, b = b % 1000000000, (a + b) % 1000000000
if n >= 0:
    if n == 0:
        print(0)
        print(0)
    else:  # n > 0
        print(1)
        print(a)
else:  # n < 0
    if m % 2 == 1:
        print(1)
        print(a)
    else:
        print(-1)
        print(a)
# 결과 : 30864kb, 284ms로 대부분의 풀이보다 더 빠르고 메모리도 절반 가까이밖에 들지 않았음
# 다만 채점결과중에 29200kb, 68ms로 통과한 사람이 있던데 확인해보니까
# 연세대학교 의대생 취미로 하는 사람이던데 재능 차이인지 지능 차이인지 참 그렇더라


