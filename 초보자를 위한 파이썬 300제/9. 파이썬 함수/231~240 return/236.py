def 함수(num):
    return num + 4

a = 함수(10)
b = 함수(a) # print를 사용할 경우 여기부터 에러가 발생함
c = 함수(b) # 이후 계산에서 계속 사용하고 싶으면 return을 사용할것
print(c)