# 리스트를 이용한 Queue 구현
# queue 라이브러리를 이용하지 않고 구현
class ListQueue:
    def __init__(self):
        self.my_list = list()

    def put(self, element):  # put 메소드, Enqueue 기능
        self.my_list.append(element)

    def get(self):  # get 메소드, Dequeue 기능
        return self.my_list.pop(0)

    def qsize(self):  # qsize 메소드, 큐의 길이 반환
        return len(self.my_list)