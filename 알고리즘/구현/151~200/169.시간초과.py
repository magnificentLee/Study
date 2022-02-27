# 1초당 제한시간 = 10 ** 8
# l초당 제한시간 = (10 ** 8) * l
# 시간초과
# 아마 팩토리얼 부분에서 시간초과가 나는 것 같음 => 정답

for _ in range(int(input())):
    s, n, t, l = input().split()
    n, t, l = int(n), int(t), int(l)
    flag, o = 1, 0
    limit = (10 ** 8) * l
    if s == "O(N)":
        o = n * t
    elif s == "O(N^2)":
        o = (n ** 2) * t
    elif s == "O(N^3)":
        o = (n ** 3) * t
    elif s == "O(2^N)":
        o = (2 ** n) * t
    elif s == "O(N!)":
        o = t
        for i in range(1, n + 1):
            o *= i
            if limit < o:
                flag = 0
                break
    if limit < o:
        flag = 0
    if flag:
        print("May Pass.")
    else:
        print("TLE!")