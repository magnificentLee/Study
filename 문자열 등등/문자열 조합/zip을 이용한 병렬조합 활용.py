# 백준 4246, 주어진 문자열을 i + 1 마다 역순으로 돌려서 동일열 다른 행의 문자들을 한줄로 출력시키기
# 2중 for문으로 출력하는 방식도 있지만 zip으로 병렬조합을 해보자
while True:
    n = int(input())
    if n == 0:
        break
    s = input()
    l = len(s) // n
    array = []
    idx = 0
    for i in range(l):
        if (i + 1) % 2 != 0:
            array.append(s[idx:idx + n])
        else:
            array.append(reversed(s[idx:idx + n]))
        idx += n
    for i in zip(*array):
        print(*i, sep="", end="")
    print()