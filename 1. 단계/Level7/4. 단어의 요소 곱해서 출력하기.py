t = int(input())

for i in range(t):
    a, b = input().split()
    text = ""
    for j in b:
        text += j * int(a)
    print(text)

