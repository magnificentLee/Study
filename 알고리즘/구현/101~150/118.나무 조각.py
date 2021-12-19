# 버블정렬, 정석적인 방법
array = list(map(int, input().split()))
l = len(array)
for i in range(l):
    for j in range(1, l):
        if array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            print(*array)
