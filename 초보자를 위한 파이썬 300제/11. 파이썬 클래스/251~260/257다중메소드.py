class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))
        # 메소드 안에서 메소드 호출 : self를 붙일것
        # self 없이 메소드 이름만 사용하면 클래스 바깥쪽 함수를 호출하는것

areum = Human("아름", 25, "여자")
areum.who()  # Huamn.who(areum)