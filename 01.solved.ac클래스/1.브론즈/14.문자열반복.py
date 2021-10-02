# 1차
"""
t = int(input())

for _ in range(t):
    r, s = input().split()
    s_list = list(s)
    for i in s_list:
        print(i * int(r), end="")
    print()
"""
# 이전에 했던 방법
t = int(input())

for _ in range(t):
    r, s = input().split()
    test = ""
    for i in s:
        test += int(r) * i
    print(test)