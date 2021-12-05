# abcdefghijklm 일 때, (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l+m) % 10 = 0
# 9788968322*73 138
# 97889683227*3 124  *의 idx * 3
# 빠른 입력을 사용해도 시간이 줄어들지 않음
array = input()
result, idx, res = 0, 0, 0
for i in range(13):
    if array[i] != "*":
        if (i + 1) % 2 == 0:
            result += int(array[i]) * 3
        else:
            result += int(array[i])
    else:  # if array[i] == "*"
        idx = i + 1
tmp = result
while True:
    res += 1
    if idx % 2 == 0:
        tmp += res * 3
    elif idx % 2 != 0:
        tmp += res
    if tmp % 10 == 0:
        print(res % 10)  # 97389414*4397 처럼 0이 정답인 경우 10이 출력되는 것을 방지
        break
    tmp = result