# 절반으로 잘랐을 때 구할 수 있는 최대 버섯 개수를 물어보는중
# 절반으로 잘랐을 경우 4개의 피자조각을 얻게되므로 반복문으로 4번 돌리면된다
array = [int(input()) for _ in range(8)]
result = 0
for i in range(8):
    tmp = 0  # max 값
    for j in range(4):
        tmp += array[j]
    if tmp > result:
        result = tmp
    array.append(array[0])
    del array[0]
print(result)