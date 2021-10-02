list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392,2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
    print(number1 + number2 + number3)
# 예상 : 인덱스가 같은 값끼리 더해줘서 총 4개의 결과가 나올것
# 결과
# 493
# 124
# 66
# 305