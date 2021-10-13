t = int(input())
string = [list(input().split()) for _ in range(t)]
for i in range(t):
    for j in string[i]:
        print("".join(reversed(list(j))), end=" ")
    print()