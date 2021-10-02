# 풀이 (c^2 == a^2 + b^2) 최댓값의 순서가 없다는점에 주의
while True:
    n = list(map(int, input().split()))
    n.sort()
    if n.count(0) > 0:
        break
    if n[2] ** 2 == (n[0] ** 2) + (n[1] ** 2):
        print("right")
    else:
        print("wrong")