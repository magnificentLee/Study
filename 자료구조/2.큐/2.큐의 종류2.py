# LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조(Stack과 동일)
# 후입선출(LIFO)
import  queue

data_queue = queue.LifoQueue()
data_queue.put(1)  # 1
data_queue.put(2)  # 2 - 1
data_queue.put(3)  # 3 - 2 - 1
data_queue.get()  # 3 출력
data_queue.get()  # 2 출력
print(data_queue.get())  # 터미널에 1출력
