# 각 줄 당 3 * m 개의 정수가 주어짐
def turn(num):
    if 0 <= num < 510000:
        return "#"
    elif 510000 <= num < 1020000:
        return "o"
    elif 1020000 <= num <1530000:
        return "+"
    elif 1530000 <= num <2040000:
        return "-"
    else:
        return "."


n, m = map(int, input().split())
array = ["" for i in range(n)]
for i in range(n):
    int_tmp = list(map(int, input().split()))
    tmp = 0
    for j in range(3 * m):
        if (j + 1) % 3 == 1:
            tmp += 2126 * int_tmp[j]
        elif (j + 1) % 3 == 2:
            tmp += 7152 * int_tmp[j]
        elif (j + 1) % 3 == 0:
            tmp += 722 * int_tmp[j]
            str_tmp = turn(tmp)
            array[i] += str_tmp  # array 부분에서 인덱스에 잘못 접근해서 오류 찾느라 오래걸렸음
            tmp = 0
for i in array:
    print(*i, sep="")