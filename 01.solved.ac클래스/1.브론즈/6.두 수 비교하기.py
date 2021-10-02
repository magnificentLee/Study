# 시도1 72ms 106B
"""
a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
"""
# 시도2 64ms 107B
a, b = map(int, input().split())
if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")