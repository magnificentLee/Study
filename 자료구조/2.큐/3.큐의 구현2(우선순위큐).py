# 리스트로 PriorityQueue (우선순위큐) 구현
class ListPriorityQueue:
    def __init__(self):
        self.my_list = list()

    def put(self, element):  # 값을 입력한 뒤 바로 정렬하는 것을 알 수 있음
        self.my_list.append(element)
        self.my_list.sort(key=lambda x: x[0])  # 값의 첫 번째, 우선순위에 해당하는 값

    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)