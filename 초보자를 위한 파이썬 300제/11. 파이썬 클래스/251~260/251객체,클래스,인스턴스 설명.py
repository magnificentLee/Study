# https://wikidocs.net/28
"""
과자 틀 = 클래스
과자 틀에 의해서 만들어진 과자 = 객체
객체와 인스턴스의 차이:
a = Cookie() 에서 a는 객체이다
그리고 a 객체는 Cookie의 인스턴스이다
관계 위주로 설명할 때 사용된다.
"a는 인스턴스", "a는 Cookie의 객체" 보다는
"a는 객체", "a는 Cokkie의 인스턴스" 라는 표현이 맞다는 말이다.

1. 계산기 함수를 생각해보자
result1 = 0
result2 = 0

def add1(num):
    global result1 global = 전역변수
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
계산기가 늘어날수록, 기능이 추가 될 수록
전역 변수와 함수를 추가해야되기 때문에
갈수록 어려워질 것이다.
2.계산기 클래스를 생각해보자
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

여기서 빼기 기능을 추가하고자 한다면
클래스 안에 다음과 같은 기능 함수를 추가하면 된다
def sub(self, num):
        self.result -= num
        return self.result
"""