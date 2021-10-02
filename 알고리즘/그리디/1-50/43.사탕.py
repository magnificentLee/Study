t = int(input())
for _ in range(t):
    candy, amount = map(int, input().split())
    box = []
    count = 0
    for _ in range(amount):
        r, c = map(int, input().split())
        box.append(r * c)
    box.sort(reverse=True)
    for i in range(len(box)):
        candy -= box[i]
        count += 1
        if candy <= 0:
            break
    print(count)


# 초기 풀이 : 출력 방식을 바꿨음에도 33퍼센트에서 오답 출력
"""
t = int(input())
for _ in range(t):
    candy, amount = map(int, input().split())
    box = []
    count = 0
    for _ in range(amount):
        r, c = map(int, input().split())
        box.append(r * c)
    box.sort(reverse=True)
    for i in range(len(box)):
        if candy <= max(box):
            count += 1
            break
        else:  # candy > box[i]
            candy -= box[i]
            count += 1
    print(count)
"""
