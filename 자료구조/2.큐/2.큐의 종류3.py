# PriorityQueue() : 우선순위큐
# 데이터마다 우선순위를 지정하여, 정렬된 큐로, 우선순위가 높은 순으로 출력하는 자료 구조
# (우선순위, 값), 우선순위는 낮을 수록 순위가 높음
# 밑에 구현 예제를 보면 알겠지만 값이 들어가면 자동으로 정렬해주는 것 같음
import queue

data_queue = queue.PriorityQueue()
data_queue.put((10, 1))  # (10, 1)
data_queue.put((5, 2))  # (5, 2) - (10, 1)
data_queue.put((15, 3))  # (5, 2) - (10, 1) - (15, 3)
data_queue.get()  # (5, 2) 출력
data_queue.get()  # (10, 1) 출력
print(data_queue.get())  # (15, 3) 출력
