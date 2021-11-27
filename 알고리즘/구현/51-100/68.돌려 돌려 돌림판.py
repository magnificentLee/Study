for _ in range(int(input())):
    n, m = map(int, input().split())  # m = 숫자 길이(ex)두자리수 = 2)
    x = int("".join(input().split()))
    y = int("".join(input().split()))
    z = list(map(str, input().split()))
    for i in range(m - 1):  # 리스트 뒷부분을 위한 숫자 추가
        z.append(z[i])
    result = 0
    for i in range(n):
        tmp = ""
        for j in range(i, i + m):
            tmp += z[j]
        if x <= int(tmp) <= y:
            result += 1
    print(result)