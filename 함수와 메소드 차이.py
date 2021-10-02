"""
함수 : 특정 작업을 수행하는 코드 조각
전역, 지역에서 독립된 기능을 수행함

메소드 : 클래스, 구조체, 열거형에 포함되어있는 함수
다른말로 클래스 함수라고도 함
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
# 메소드 안에서 메소드 호출 : self를 붙일것
# self 없이 메소드 이름만 사용하면 클래스 바깥쪽 함수를 호출하는것
"""