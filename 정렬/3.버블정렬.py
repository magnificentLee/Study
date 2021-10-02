t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))
# Bubble Sort : 버블정렬
for i in range(t):  # t 혹은 len(n)
    for j in range(t):  # t 혹은 len(n)
        if n[i] < n[j]:
            n[i], n[j] = n[j], n[i]
for j in n:
    print(j)