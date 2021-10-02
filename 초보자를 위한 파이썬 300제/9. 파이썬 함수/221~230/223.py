# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.


def print_even(my_list):
    for i in my_list:
        if i % 2 == 0:
            print(i)


print_even([1, 3, 2, 10, 12, 11, 15])