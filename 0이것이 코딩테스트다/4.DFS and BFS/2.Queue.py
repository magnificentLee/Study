# queue : 선입선출   queue 구현을 위해 deque를 사용할 것
# deque 는 스택과 큐의 장점을 모두 채택한 것으로 데이터를 넣고 빼는 속도가 리스트 자료형에 비해
# 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다.
# deque는 collections 모듈에서 제공함
from collections import deque
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # 선입선출, 제일 왼쪽 5 제거
queue.append(1)
queue.append(4)
queue.popleft()  # 2 제거
print(queue)