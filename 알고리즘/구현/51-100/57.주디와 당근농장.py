# r + c 가 2로 나누어 떨어지면 i + j가 2로 나누어 떨어지면 v 아니면 .
# r + c 가 2로 나우어 떨어지지 않으면 i + j가 2로 나누어 떨어지지 않으면 . 아니면 v
n, r, c = map(int, input().split())
if (r + c) % 2 == 0:
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("v", end="")
            else:
                print(".", end="")
        print()
else:
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print(".", end="")
            else:
                print("v", end="")
        print()
