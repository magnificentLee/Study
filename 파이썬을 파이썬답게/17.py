"""
def solution(n):
    global total
    total *= n
    for i in range(1, total // 2 + 1):
        if i ** 2 == total:
            return 0
    return 1

n_list = [int(input()) for _ in range(5)]
total = 1
for i in n_list:
    if solution(i) == 0:
        print("found")
        break
else:
    print("not found")
"""
import math
def solution(n):
    total = 1
    for i in n:
        total *= i
        if math.sqrt(total) == int(math.sqrt(total)):
            print("found")
            return False
    return True

n_list = [int(input()) for _ in range(5)]
if solution(n_list):
    print("not found")