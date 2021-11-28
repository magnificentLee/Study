# 2008 -> 8200 - 0028 : 즉, sorted로 reverse
# 시작값을 계산 결과로 최신화 해주면서 반복문 진행
# 반례
# 1000 -> 1000 - 0001 = 0999, 0999 -> 9990-0999 = 8991
# but 1000 - 0001 = 999, 999 -> 999 - 999 = 0
for _ in range(int(input())):
    n = input()
    count = 0
    while True:
        front, back = "", ""
        for i in sorted(n, reverse=True):
            front += i
        for i in sorted(n):
            back += i
        result = str(int(front) - int(back))
        if len(result) < 4:
            result += "0"
        if n == result:
            print(count)
            break
        else:
            count += 1
            n = result