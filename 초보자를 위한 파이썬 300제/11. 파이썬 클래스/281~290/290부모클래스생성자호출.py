class 부모:
    def __init__(self):
        print("부모생성")


class 자식(부모):
    def __init__(self):
        print("자식생성") # 순서 : 자식 - 부모
        super().__init__()
        # print("자식생성") 순서: 부모 - 자식


나 = 자식()