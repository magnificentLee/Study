n = int(input())

array = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))
for i in targets:
    if i in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")