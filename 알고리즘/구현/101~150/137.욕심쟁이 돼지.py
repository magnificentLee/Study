# 자신과 양쪽과 맞은편을 더한값이 다음날
# 21
# 1  2  3  4  5  6   21
# 13 11 15 13 17 15  84
# 52 56 54 58 56 60  336
# 즉, 전체의 값은 이전날의 4배임
t = int(input())
for _ in range(t):
    n = int(input())
    array = map(int, input().split())
    total = sum(array)
    day = 1
    while True:
        if total > n:
            break
        total *= 4
        day += 1
    print(day)