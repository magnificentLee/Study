t = int(input())

for i in range(t):
    n = input()
    if len(n) == 1:
        print(n * 2)
    else:
        print(n[0] + n[len(n) - 1])
