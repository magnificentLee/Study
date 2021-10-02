for _ in range(int(input())):
    n = list(input())
    result = 0
    point = 1
    for i in n:
        if i == "O":
            result += point
            point += 1
        else:
            point = 1
    print(result)