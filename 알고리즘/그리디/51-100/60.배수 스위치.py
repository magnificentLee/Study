# i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다.
# insert 함수를 이용해 i = 0 을 추가해준다
def switch(array):
    result = 0
    for i in range(0, len(array)):
        if array[i] == "Y":
            for j in range(i, len(array), i):
                if array[j] == "Y":
                    array[j] = "N"
                else:
                    array[j] = "Y"
            result += 1
    return result


bulbs = list(input())
bulbs.insert(0, "N")
print(switch(bulbs))