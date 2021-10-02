import sys
from collections import deque

queue = deque()

def push_front(n):
    return queue.appendleft(n)
def push_back(n):
    return queue.append(n)
def pop_front():
    return queue.popleft() if queue else -1
def pop_back():
    return queue.pop() if queue else -1
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
    s = a[0]  # string
    if s == "push_front":
        push_front(a[1])
    elif s == "push_back":
        push_back(a[1])
    elif s == "pop_front":
        print(pop_front())
    elif s == "pop_back":
        print(pop_back())
    elif s == "size":
        print(size())
    elif s == "empty":
        print(empty())
    elif s == "front":
        print(front())
    elif s == "back":
        print(back())
