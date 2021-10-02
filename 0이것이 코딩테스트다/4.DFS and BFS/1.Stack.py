# stack 의 기본적인 예시
# 삽입(5) 삽입(2) 삽입(3) 삽입(7) 삭제() 삽입(1) 삽입(4) 삭제() 의 순서로 진행할 때
# 선입후출
stack = []
stack.append(5)
print(stack)

stack.append(2)
print(stack)

stack.append(3)
print(stack)

stack.append(7)
print(stack)

stack.pop()  # 선입후출, 제일 우측; 7 제거
print(stack)

stack.append(1)
print(stack)

stack.append(4)
print(stack)

stack.pop()  # 제일 우측; 4 제거
print(stack)