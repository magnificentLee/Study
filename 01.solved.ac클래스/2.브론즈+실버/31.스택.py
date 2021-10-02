# 이상적인 답안
"""
import sys

def push(n):
    stack.append(n)
def pop():
    if not stack:
        return -1
    else:
        return stack.pop()
def size():
    return len(stack)
def empty(): # 스택이 비어있다면
    return 0 if stack else 1
def top():  # 가장 먼저 들어간게 왼쪽 끝(가장 아래)에 있으므로
    return stack[-1] if stack else -1
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    a = sys.stdin.readline().rstrip().split()
    lang = a[0]
    if lang == "push":
        push(int(a[1]))
    elif lang == "pop":
        print(pop())
    elif lang == "size":
        print(size())
    elif lang == "empty":
        print(empty())
    elif lang == "top":
        print(top())
"""
import sys

def push(n):
    stack.append(n)
def pop():
    if not stack:
        return -1
    else:
        return stack.pop()
def size():
    return len(stack)
def empty():
    if not stack:
        return 1
    else:
        return 0
def top():
    if stack:
        return stack[-1]
    else:
        return -1

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    a = sys.stdin.readline().rstrip().split()
    string = a[0]
    if string == "push":
        push(a[1])
    elif string == "pop":
        print(pop())
    elif string == "size":
        print(size())
    elif string == "empty":
        print(empty())
    elif string == "top":
        print(top())