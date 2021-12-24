# c 등장 이전까지 -1, c = 0, c 등장 이후로 1 씩 증가, 다시 c를 만나면 다음 수는 1로 초기화후 증가
h, w = map(int, input().split())
array = []
for _ in range(h):
    n = input()
    tmp = -1
    result = []
    for i in n:
        if i == "c":
            i = "0"
            tmp = 1
        else:
            if tmp == -1:
                i = tmp
            else:
                i = tmp
                tmp += 1
        result.append(i)
    array.append(result)
for i in array:
    print(*i)