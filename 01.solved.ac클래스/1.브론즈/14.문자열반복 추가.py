for _ in range(int(input())):
    n, s = input().split()
    result = ""
    for i in s:
        result += i * int(n)
    print(result)