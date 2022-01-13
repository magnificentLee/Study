# 파이썬으로 Node의 구현
# 노드는 data를 저장하는 변수와 다음 노드를 가리키는 포인터로 구성됨
# 여기서는 data, next 라는 변수로 정했음
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
