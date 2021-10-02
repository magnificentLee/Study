# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을
# 화면에 출력하는 print_keys 함수를 정의하라.


def print_keys(my_dict):
    for i in my_dict.keys():
        print(i)


print_keys({"이름":"김말똥", "나이":30, "성별":0})