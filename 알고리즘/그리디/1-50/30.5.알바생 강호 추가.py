from sys import stdin as st

n = int(st.readline())

p = sorted([int(st.readline()) for _ in range(n)], reverse=True)
result = 0
tips = 0
for i in range(n):
    tips = p[i] - ((i + 1) - 1)
    if tips < 0:
        tips = 0
    result += tips
print(result)