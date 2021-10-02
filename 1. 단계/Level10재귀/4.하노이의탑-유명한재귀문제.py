def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, end, mid)
        print(start, end)
        hanoi(n - 1, mid, start, end)

n = int(input())
total = 0
for i in range(n):
    total = total * 2  # 원판을 두 곳(중간지점, 목적지)을 이동해야 되기 때문
    total += 1  # 제일 아래 원판을 더해야 됨
print(total)
hanoi(n, 1, 2, 3)

"""
def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:  # n == 1 일 때까지 계속 재귀
        hanoi(n - 1, a, c, b)
        move.append([a, c])
        hanoi(n - 1, b, a, c)


move = []
hanoi(int(input()), 1, 2, 3)

print(len(move))
print("\n".join([" ".join(str(i) for i in row) for row in move]))
"""

"""
def hanoi(disk, start, mid, end):  # 출발지, 중간, 목적지
    if disk == 1:
        print(start, end)  # 시작점, 도착점
    else:
        hanoi(disk - 1, start, end, mid)  # 맨 밑을 제외한 원반들을 중간지점으로 옮김
        print(start, end)  # 맨 아래 원반을 목적지로 이동
        hanoi(disk - 1, mid, start, end)  # 중앙에 있는것들을 목적지로 이동
        
total_disk = int(input())
total_movement = 0

for disk in range(total_disk):
    total_movement = total_movement * 2
    total_movement += 1

print(total_movement)
hanoi(total_disk, 1, 2, 3)
# 또는
disk = int(input())
print((2 ** disk) - 1)
hanoi(disk, 1, 2, 3)
"""
