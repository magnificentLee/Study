# 파이썬으로 Linked List의 구현
# 간단한 코드 구현만 했음, 중간 데이터 삽입 코드는 작성하지 않음
class Node:
    def __init__(self, data):
        self.data = data  # 저장된 데이터
        self.next = None  # 다음 노드를 가리키는 포인터


class LinkedList:
    def __init__(self):
        self.head = None  # 첫 생성시 내부에는 노드가 없으므로

    def add(self, data):
        new_node = Node(data)
        if not self.head:  # 처음 노드가 아닌 경우
            self.head = new_node
        else:  # 처음 노드인 경우
            node = self.head  # 노드 = 헤드 노드(시작노드)
            while node.next:
                node = node.next
            node.next = new_node

    def delete(self, data):
        node = self.head
        if node.data == data:  # 찾으려는 데이터를 발견했으면
            self.head = node.next  # head를 현재 head의 next. 즉, 다음 노드로 변경
            del node
        else:  # 발견하지 못했다면
            while node.next:  # 포인터를 늘려서 데이터를 찾자
                next_node = node.next
                if next_node.data == data:  # 데이터를 발견했다면
                    node.next = next_node.next  # 다음 포인터와 연결 및 삭제
                    del next_node
                else:
                    node = node.next

    def find(self, data):  # 노드의 메모리를 찾는 메소드
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


li = LinkedList()
li.add(1)
li.add(2)
li.add(3)
print(li.find(3))  # find 함수 = 데이터값으로 Node의 메모리를 찾아줌
li.print()

li.delete(2)
li.print()

li.delete(1)
li.print()
li.delete(3)
print(li.head)