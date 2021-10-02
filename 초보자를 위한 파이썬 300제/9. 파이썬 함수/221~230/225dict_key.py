my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는
# print_value_by_key 함수를 정의하라


def print_value_by_key(my_dict, key):
    print(my_dict[key])


print_value_by_key(my_dict, "10/26")
print_value_by_key(my_dict, "10/27")
# 특정 key 값의 value를 가져오는 방법 = 87 참고
#예시
#my_dict = {"일": 1, "십": 10, "백": 100}
#print(my_dict["일"])
#결과는 1 이 나옴