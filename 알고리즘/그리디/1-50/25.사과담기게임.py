from sys import stdin
n, m = map(int, stdin.readline().split())  # m = 시작지점X, 바구니의 크기임
j = int(stdin.readline())
start = 1
end = m
distance = 0
for _ in range(j):
    location = int(stdin.readline())
    if location < start:
        distance += start - location
        start = location
        end = location + m - 1  # 1 = 첫 시작지점
    elif location > end:
        distance += location - end
        end = location
        start = end - m + 1  # 1 = 첫 시작지점
    # 겹치는 경우는 이동하지 않으므로 세지 않는다
print(distance)