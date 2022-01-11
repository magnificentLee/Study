# Queue() : 일반적인 큐 자료구조
import queue

data_queue = queue.Queue()
data_queue.put(1)  # 1
data_queue.put(2)  # 1 - 2
data_queue.put(3)  # 1 - 2 - 3
data_queue.get()  # 1 출력
data_queue.get()  # 2 출력
print(data_queue.get())  # 터미널에 3이 출력됨
