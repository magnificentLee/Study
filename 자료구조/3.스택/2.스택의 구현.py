# 리스트로 스택 구현하기
class ListStack:
    def __init__(self):
        self.my_list = list()

    def push(self, data):
        self.my_list.append(data)

    def pop(self):
        return self.my_list.pop()
        # pop(0)이 아님 = 마지막(뒤)의 데이터를 먼저 꺼냄
