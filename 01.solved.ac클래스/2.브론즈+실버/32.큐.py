import sys
queue = []

def push(n):
    return queue.append(n)
def pop():
    return queue.pop(0) if queue else -1
def size():
    return len(queue)
def empty():
    return 1 if not queue else 0
def front():
    return queue[0] if queue else -1
def back():
    return queue[-1] if queue else -1

n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().rstrip().split()
    s = a[0]
    if s == "push":
        push(a[1])
    elif s == "pop":
        print(pop())
    elif s == "size":
        print(size())
    elif s == "empty":
        print(empty())
    elif s == "front":
        print(front())
    elif s == "back":
        print(back())

# 덱 = deque 이므로 문제가 원하는건 이게 아님
# 따라서 아래 방식은 덱 문제에 맞는 풀이임
"""
import sys
from collections import deque

queue = deque()

def push(n):
    queue.append(n)
def pop():
    return -1 if not queue else queue.popleft()
# deque를 사용할 경우 pop 대신 popleft를 써야함
def size():
    return len(queue)
def empty():
    return 0 if queue else 1
def front():
    return queue[0] if queue else -1
def back():
    return queue[-1] if queue else -1

n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().rstrip().split()
    s = a[0]
    if s == "push":
        push(a[1])
    elif s == "pop":
        print(pop())
    elif s == "size":
        print(size())
    elif s == "empty":
        print(empty())
    elif s == "front":
        print(front())
    elif s == "back":
        print(back())
"""