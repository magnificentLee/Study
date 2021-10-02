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