class Stack:
    def __init__(self):  # 생성함수
        self.items = []  # 데이터 저장을 위한 리스트를 준비한다.(값들이 저장될 곳)

    def push(self, val):
        self.items.append(val)  # append함수를 활용해서 push()를 만들었다
        # push(self, val) --> self라는 객체(스택)에 val을 넣어라

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
            # pop할 item이 없으면 IndexError가 발생하고,
            # 'Stack is empty'라는 메시지가 뜬다

    def top(self):  # pop()과는 달리 그냥 맨 위에 있는 item이 뭔지 보여주기만 함(삭제하지 않는다!!!)
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):  # len()호출시, stack item 수 반환
        return len(self.items)

    def isEmpty(self):  # stack이 비어있는지를 판단. 길이가 0인지?
        return len(self) == 0