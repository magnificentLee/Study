n = int(input())
count = 1  # 지나가는 방 수 1 2 3 4
first = 1  # 숫자범위들 1(초기값) 7 19 37 61
number = 6  # 개  6 12 18 24...
while n > first:
    count += 1  # 방의 개수 1 2 3 4
    first += number  # 1 7 19 37 61
    number += 6  # 6 12 18 24...
print(count)
